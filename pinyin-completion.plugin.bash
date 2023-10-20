. "$(dirname "${BASH_SOURCE[0]}")/common.sh"

_pinyin_comp() {
	# unix file names can contain '\n', so use '\0' to separate them
	local IFS=$'\0' suffix
	if [ "$1" = x-d ]; then
		suffix=/
	else
		suffix=''
	fi
	for file in "$(dirname "$2")"/*"$suffix"; do
		file="${file#./}"
		if [[ $file =~ [^[:ascii:]] ]]; then
			result="$(pypinyin -fslug -sz -p= "$file")"
			for k in "${!FUZZY[@]}"; do
				v="${FUZZY[$k]}"
				result="${result//$k/$v}"
			done
			for k in "${!_punctuation_map[@]}"; do
				v="${_punctuation_map[$k]}"
				result="${result//$k/$v}"
			done
		else
			result="$file"
		fi
		if [[ $result == "$2"* ]]; then
			echo "$file"
		fi
	done
}

_filedir() {
	local IFS=$'\t\n' xspec

	_expand || return 0

	local -a toks
	local tmp

	toks=("${toks[@]-}" "$(
		compgen -d -- "$(quote_readline "$cur")" | {
			while read -r tmp; do
				echo "$tmp"
			done
		}
	)")

	if [[ $1 != -d ]]; then
		xspec=${1:+"!*.$1"}
		toks=("${toks[@]-}" "$(
			compgen -f -X "$xspec" -- "$(quote_readline "$cur")" | {
				while read -r tmp; do
					[ -n "$tmp" ] && echo "$tmp"
				done
			}
		)")
	fi
	chs=("$(_pinyin_comp "x$1" "$cur")")
	COMPREPLY=("${COMPREPLY[@]}" "${toks[@]}" "${chs[@]}")
}

_filedir_xspec() {
	local IFS cur xspec

	IFS=$'\t\n'
	COMPREPLY=()
	cur=$(_get_cword)

	_expand || return 0

	xspec="$(sed -ne $'/^complete .*[ \t]'"${1##*/}"$'\([ \t]\|$\)/{p;q;}' \
		"$BASH_COMPLETION")"
	xspec="${xspec#*-X }"
	xspec="${xspec%% *}"

	local -a toks
	local tmp

	toks=("${toks[@]-}" "$(
		compgen -d -- "$(quote_readline "$cur")" | {
			while read -r tmp; do
				# see long TODO comment in _filedir() --David
				echo "$tmp"
			done
		}
	)")

	toks=("${toks[@]-}" "$(
		eval compgen -f -X "$xspec" -- '$(quote_readline '\$cur")" | {
			while read -r tmp; do
				[ -n "$tmp" ] && echo "$tmp"
			done
		}
	)")

	chs=("$(pinyin-comp "x$1" "$cur")")
	COMPREPLY=("${toks[@]}" "${chs[@]}")
}

complete -o filenames -F _filedir_xspec file
