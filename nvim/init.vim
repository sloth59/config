
"""VIM-PLUG as plugin manager
call plug#begin('~/.config/nvim/plugged')

Plug 'jiangmiao/auto-pairs'  "auto-pair
Plug 'mattn/emmet-vim'  "emmet support
Plug 'sheerun/vim-polyglot'   "language packs
Plug 'itchyny/lightline.vim'  "status line
Plug 'dracula/vim'  "theme
" Plug 'neoclide/coc.nvim'  "auto completion engine
" Plug 'scrooloose/nerdtree'  "file explorer
" Plug 'tpope/vim-fugitive'  "git integration
" Plug 'prettier/vim-prettier'  "preetier code format
" Plug 'morhetz/gruvbox'  "theme
" Plug 'NLKNguyen/papercolor-theme'  "theme

call plug#end()


set number " show line number
syntax on  " colored syntax
set cursorline  " line with cursor is highlited


colorscheme dracula			
"""Lightline
set noshowmode
let g:lightline={ 'colorscheme': 'dracula', }


" current colorscheme follows terminal background
hi Normal ctermbg=NONE guibg=NONE
