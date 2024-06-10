# Easily Formattable Theme - EFT

EFT-py is a python library that allows developers to easily create themes for their gui applications

You can download EFT by cloning the repository, or using `pip`

```yml
pip install eft-py
```

## Why use EFT?

EFT allows the developers, and the users to create themes very easily for GUI applications that have EFT support. It is super easy to implement EFT into your project, and you can customize tons of aspects of your application, such as Colors, Integers, Booleans, Fonts etc. There is also EFT for Godot, and more in the future!

## How do I use EFT?

Here's how to get started with using EFT!

### Creating a theme

Creating a theme is simple! You just need to supply the name of the theme, and then any fields that you want! You can also create your own types using the `register_type` function! The current default types include

- String
- Color
- Int
- Bool

```eft
- Theme Name

Background: 255,255,255 : Color

FontSize: 16 : Int
Title: "My Title" : String
```

### Implementing themes

It's super easy to implement themes into your application, with just two lines of code you can grab a color, or any other property from the file!

```py
from eft import Theme

theme = Theme.EFT_Theme("examples/test.eft")

print(theme.get_property("background_color")) # Prints the background color property!
```

## Contributing

Feel free to open a Pull Request, and help contribute to EFT!
