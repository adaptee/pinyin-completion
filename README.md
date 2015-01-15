pinyin-completion
========

Complete path by acronym of pinyin initials.

用拼音补全命令行中的中文名称和路径

This is a fork for enhancement and bugs fixing.

### Enhancement

* Auto escaping for special characters.
* Fixed missing `_force_rehash()` error.

### Sample

	$ ls ./
	SVN培训  全球眼  浙江建行  浙江农信

使用: (输完后按 TAB 键自动补全)

	cd S     <tab>             进入[SVN培训]
	cd q     <tab>             进入[全球眼]
	cd z     <tab>             自动补全[浙江]
	cd zj    <tab><tab>        提示[浙江建行 浙江农信]备选
	cd zj1   <tab>             进入[浙江建行]
	cd zj2   <tab>             进入[浙江农信]
	cd 浙江j <tab>             进入[浙江建行]
	cd zjj   <tab>             进入[浙江建行]

### Install

	git clone git@github.com:petronny/pinyin-completion.git
	cd pinyin-completion
	sudo ./setup.py install

### Usage

For Bash users, source `shell/pinyin-comp.bash` in your `~/.bashrc`

For Zsh users, source `shell/pinyin-comp.zsh` in your `~/.zshrc`

### Others

`tools/table-generator.py` is used to generate `pinyin_initial.py`, based upon the contents of `tools/unicode-han-pinyin.txt`.

If you feel the default pinyin_initial.py is too big, which cause sensible delay and un-wanted ambigurous, just use you favourite editor to modify `tools/unicode-han-pinyin.txt`, then regenerate `pinyin_initial.py` by running:

	$ ./table-generate.py > pinyin_initial.py

