from eft import Theme

theme = Theme.EFT_Theme("examples/test.eft")

print(theme.get_property("background_color"))
print(theme.get_property("title"))
print(theme.get_property("number"))
print(theme.get_property("enabled"))