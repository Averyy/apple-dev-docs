# Building your project with embedded shader sources

**Framework**: Xcode

Prepare to debug your project’s shaders by including source code in the build.

#### Overview

To debug your shaders in Xcode, configure your build to include shader source code by changing your project’s build settings. Select your project in the Project navigator, click the Build Settings tab, and search for the Produce Debugging Information setting in the Metal Compiler Build Options section. Then, change the setting’s Debug entry to “Yes, include source code.”

![An Xcode screenshot showing the Build Settings for a project target, highlighting the Produce Debugging Information setting with the Debug entry set to Yes, include source code.](https://docs-assets.developer.apple.com/published/19a31b83ecf497431a95e4bda1d3ac22/gputools-metal-debugger-se-include-sources%402x.png)

Alternatively, you can debug the shaders that you compile for release by generating a separate symbol file for each Metal library in your project. For more information on using this approach, see [`Generating and loading a Metal library symbol file`](https://developer.apple.com/documentation/Metal/generating-and-loading-a-metal-library-symbol-file).

> ❗ **Important**: To ensure you don’t include debugging information in apps you ship to customers, be sure to reset the Produce Debugging Information for Release option to No when you finish debugging.

## See Also

- [Naming resources and commands](naming-resources-and-commands.md)
  Enhance the debugging of your Metal app using labels and grouping.
- [Creating and using custom capture scopes](creating-and-using-custom-capture-scopes.md)
  Capture specific GPU commands by using custom capture scopes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/building-your-project-with-embedded-shader-sources)*