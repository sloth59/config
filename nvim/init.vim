

""""""VIM-PLUG as plugin manager
call plug#begin('~/.config/nvim/plugged')

Plug 'jiangmiao/auto-pairs'  "auto-pair
Plug 'mattn/emmet-vim'  "emmet support
Plug 'sheerun/vim-polyglot'   "language packs
Plug 'NLKNguyen/papercolor-theme'  "theme
Plug 'itchyny/lightline.vim'  "status line
" Plug 'neoclide/coc.nvim'  "auto completion engine
" Plug 'scrooloose/nerdtree'  "file explorer
" Plug 'tpope/vim-fugitive'  "git integration
" Plug 'prettier/vim-prettier'  "preetier code format
" Plug 'morhetz/gruvbox'  "theme
" Plug 'dracula/vim'  "theme

call plug#end()




syntax on  " colored syntax
set cursorline  " line with cursor is highlited

colorscheme PaperColor
			
"""""""""" lines for lightline""""""""
set noshowmode
let g:lightline={
	\ 'colorscheme': 'PaperColor',
	\ }


