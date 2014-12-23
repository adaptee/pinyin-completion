### Install

	git clone git@github.com:adaptee/pinyin-completion.git
	cd pinyin-completion
	sudo ./setup.py install

### Usage

For bash users, source `shell/pinyin-comp.bash` in your `~/.bashrc`

For zsh users, source `shell/pinyin.comp.zsh` in your `~/.zshrc`

### Others

`tools/table-generator.py` is used to generate `pinyin_initial.py`, based upon the contents of `tools/unicode-han-pinyin.txt`.

If you feel the default pinyin_initial.py is too big, which cause sensible delay and un-wanted ambigurous, just use you favourite editor to modify `tools/unicode-han-pinyin.txt`, then regenerate `pinyin_initial.py` by running:

	$ ./table-generate.py > pinyin_initial.py

