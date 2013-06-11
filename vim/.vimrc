sy on
set nu
set hlsearch
highlight Search ctermbg=Blue ctermfg=Black
set nowrapscan
set laststatus=2
set statusline=%<[%n]%m%r\ %f%=\ %l,%c%V%6P%h%w%{'['.(&fenc!=''?&fenc:&enc).':'.&ff.']'}%y
set scrolloff=5
set smartindent
if exists("&ambiwidth")
    set ambiwidth=double
endif
set expandtab
set shiftwidth=4
set softtabstop=4
set tabstop=4
filetype on
set fileencodings=utf-8,cp932,euc-jp
set fileformats=unix,dos,mac
colorscheme desert
