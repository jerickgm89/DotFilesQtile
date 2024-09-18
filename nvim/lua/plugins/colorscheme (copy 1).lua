return {
  "olimorris/onedarkpro.nvim",
  priority = 1000,
  config = function()
    require("onedarkpro").setup({
      colors = {
        onedark_dark = { bg = "#1e1e2e" },
      },
      highlights = {
        Comment = { italic = true },
        Directory = { bold = true },
        ErrorMsg = { italic = true, bold = true },
      },
      styles = {
        types = "italic",
        methods = "italic",
        numbers = "bold",
        strings = "NONE",
        comments = "italic, bold",
        keywords = "italic",
        constants = "italic, bold",
        functions = "italic",
        operators = "italic, bold",
        variables = "italic",
        parameters = "italic",
        conditionals = "italic",
        virtual_text = "NONE",
      },
    })
  end,
}
