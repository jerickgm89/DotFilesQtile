local keymap = vim.keymap
local opts = { noremap = true, silent = true }
-- REQUIRED
local harpoon = require("harpoon")
harpoon:setup()
local Oil = require("oil")
Oil:setup()
-- REQUIRED
-- Increment/decrement
keymap.set("n", "+", "<C-a>")
keymap.set("n", "-", "<C-x>")

-- Delete a word backwards
keymap.set("n", "e,", 'vb"_d')

-- Select all
keymap.set("n", "<C-a>", "gg<S-v>G")

-- Save with root permission (not working for now)
--vim.api.nvim_create_user_command('W', 'w !sudo tee > /dev/null %', {})

-- Disable continuations
keymap.set("n", "<Leader>o", "o<Esc>^Da", opts)
keymap.set("n", "<Leader>O", "O<Esc>^Da", opts)

-- Jumplist
keymap.set("n", "<C-m>", "<C-i>", opts)

-- New tab
keymap.set("n", "te", ":tabedit")
keymap.set("n", "<tab>", ":tabnext<Return>", opts)
keymap.set("n", "<s-tab>", ":tabprev<Return>", opts)
-- Split window
keymap.set("n", "ss", ":split<Return>", opts)
keymap.set("n", "sv", ":vsplit<Return>", opts)
-- Move window
keymap.set("n", "sd", "<C-w>h")
keymap.set("n", "st", "<C-w>k")
keymap.set("n", "sh", "<C-w>j")
keymap.set("n", "sn", "<C-w>l")

-- Resize window
keymap.set("n", "<C-w><left>", "<C-w><")
keymap.set("n", "<C-w><right>", "<C-w>>")
keymap.set("n", "<C-w><up>", "<C-w>+")
keymap.set("n", "<C-w><down>", "<C-w>-")

-- Diagnostics
keymap.set("n", "<C-j>", function()
  vim.diagnostic.goto_next()
end, opts)

-- OIL --
keymap.set("n", "<Leader>-", "<CMD>Oil<CR>", { desc = "Open parent directory" })

-- Delete all buffers but the current one --
vim.keymap.set(
  "n",
  "<leader>bq",
  '<Esc>:%bdelete|edit #|normal`"<Return>',
  { desc = "Delete other buffers but the current one" }
)

----- HARPOON 2 -----
keymap.set("n", "<leader>a", function()
  harpoon:list():add()
end, { desc = "Add harpoon mark" })

keymap.set("n", "<C-e>", function()
  harpoon.ui:toggle_quick_menu(harpoon:list())
end)

keymap.set("n", "<C-M-h>", function()
  harpoon:list():select(1)
end)

keymap.set("n", "<C-M-j>", function()
  harpoon:list():select(2)
end)

keymap.set("n", "<C-M-k>", function()
  harpoon:list():select(3)
end)

keymap.set("n", "<C-M-l>", function()
  harpoon:list():select(4)
end)
