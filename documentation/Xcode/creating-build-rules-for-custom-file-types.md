# Creating build rules for custom file types

**Framework**: Xcode

Tell Xcode how to build your project’s custom file types, and provide dependency information to optimize the build process for each file.

#### Overview

The code and resource files in a project are typically in an editable format that a running app can’t use directly. During a build, Xcode transforms the files you’ve been editing into a suitable runtime format. For example, it compiles your code files into machine instructions for a specific device. Each transformation requires a specific tool, and Xcode uses your project’s build rules, or the built-in build rules, to select the correct tool for each file type.

A build rule maps a specific file type to the tools Xcode needs to generate the required output for that file. For example, one build rule compiles `.swift` files into executable code using the Swift compiler. Xcode contains built-in rules for many file types, including both code files and resource files. You can create additional rules to transform other file types into an appropriate final form, or override a built-in rule to use a different tool.

> **Note**: A build rule is the preferred way to process files that are independent from each other. The build system processes each file using a separate task, which allows for more parallelization. If you require the build system to process your files as a group in a single operation, create a custom Run Script build phase instead, as described in [`Running custom scripts during a build`](running-custom-scripts-during-a-build.md).

A build rule is the preferred way to process files that are independent from each other. The build system processes each file using a separate task, which allows for more parallelization. If you require the build system to process your files as a group in a single operation, create a custom Run Script build phase instead, as described in [`Running custom scripts during a build`](running-custom-scripts-during-a-build.md).

##### Add a New Build Rule for a Custom File Type

If your project contains file types not covered by Xcode’s built-in build rules, you can add new build rules to address those types. To create a new build rule:

1. In the project editor, select the target that contains your custom files.
2. Click the Build Rules tab.
3. Click the Add button (+) to create a new rule.
4. In the Process field, specify a filename matching string.
5. In the script text field, specify your custom script code.

![A target contains a custom build rule that builds a custom file type using a shell script.](https://docs-assets.developer.apple.com/published/a23b1bb936328f1861ce2bb80e67b6d1/build-rules-creating%402x.png)

A build rule can use either a custom shell script or an existing tool to process files. If you use an existing tool to handle your custom file types, select that tool from the build rule’s Using field. For example, if your input files contain source code that a built-in compiler can handle, select the compiler from the list.

##### Specify the Match Criteria for Source Files

To match custom file types, select the “Source files with names matching” option in the Process field and specify a custom pattern string. Specify pattern strings that follow the same rules as the `fnmatch` function in the Standard C library. For example, to match all files with the names `myfile.c` and `myfile.h`, specify the string `*/myfile.c */myfile.h`. During a build, Xcode compares the full path of each project file against the specified pattern. When a match occurs, the system executes your custom script code.

> ❗ **Important**: Avoid choosing filename extensions that overlap with the extensions other file types use. Xcode selects the first rule that matches a given file, so any overlap might cause Xcode to run the wrong tool.

Avoid choosing filename extensions that overlap with the extensions other file types use. Xcode selects the first rule that matches a given file, so any overlap might cause Xcode to run the wrong tool.

For information about pattern matching using the `fnmatch` function, see the man page for that function.

##### Specify the Input and Output Files for Your Shell Script

When Xcode detects one of your custom file types, it executes the shell script associated with the matching build rule. In your script, get the path to the source file from the `SCRIPT_INPUT_FILE` environment variable, and begin processing the file. If your script requires additional input data, such as build configuration files, specify those files in the Input Files section of your build rule, and access them using environment variables.

Your script code takes an input source file and generates an appropriate output file. For example, a script that compiles source code might generate an object file with machine instructions. You specify the output files for your script in the Output Files section of your build rule. Most scripts generate only one output file, but you can specify multiple files when appropriate. Xcode determines when to rebuild your source files based on the output files that you declare. When the source file is newer than the output files, Xcode rebuilds it. If you don’t specify any output files, Xcode builds your source file every time, regardless of whether the source file changed.

When you specify input and output files in your build rule, use the following variables to compose the path and filename information. For example, you might use `$(DERIVED_FILE_DIR)/$(INPUT_FILE_BASE).compiledData` to specify an output file based on the name of the original source file.

| Variable | Description |
| --- | --- |
| `PROJECT_DIR` | The root directory of your project’s source files. |
| `DERIVED_FILE_DIR` | The directory in which to place generated output files. The build system manages this directory and can clean it when needed. |
| `INPUT_FILE_BASE` | The base name of the script’s input file. For example, if the path to the input file is `$PROJECT_DIR/Images/Default.png`, this variable contains the value `Default`. |
| `INPUT_FILE_NAME` | The name of the input file, including the filename extension. For example, if the path to the input file is `$PROJECT_DIR/Images/Default.png`, this variable contains the value `Default.png`. |
| `INPUT_FILE_DIR` | The directory that contains the input file. For example, if the path to the input file is  `$PROJECT_DIR/Images/Default.png`, this variable points to the `Images` directory in your project. |
| `INPUT_FILE_PATH` | The complete path to the input file. |

> ❗ **Important**: Place your script’s output files in the directory represented by the `DERIVED_FILE_DIR` variable. If you place them in other locations, your version-control system might not find them, or Xcode might not be able to remove them during a clean build operation.

Place your script’s output files in the directory represented by the `DERIVED_FILE_DIR` variable. If you place them in other locations, your version-control system might not find them, or Xcode might not be able to remove them during a clean build operation.

##### Access Script Related Files From Environment Variables

Shell scripts have access to the current target’s build settings and the input and output files associated with the build rule. Before executing your build rule’s script, Xcode configures the shell environment with several environment variables. To access the build rule’s input and output files, use the environment variables in the following table.

| Variable | Description |
| --- | --- |
| `SCRIPT_INPUT_FILE` | The absolute path of the file to process. |
| `OTHER_INPUT_FILE_FLAGS` | Additional command-line flags you assigned to the file in the Compile Sources build phase. |
| `SCRIPT_INPUT_FILE_COUNT` | The number of paths in the Input Files section of your build rule. |
| `SCRIPT_INPUT_FILE_` | The absolute path to one of the files in the Input Files section of your build rule. Xcode creates an environment variable for each file, starting with `SCRIPT_INPUT_FILE_0` and increasing the number value sequentially for each subsequent file in the list. |
| `SCRIPT_OUTPUT_FILE_COUNT` | The number of paths in the Output Files section of your build rule. |
| `SCRIPT_OUTPUT_FILE_` | The absolute path to one of the files in the Output Files section of your build rule. Xcode creates an environment variable for each file, starting with `SCRIPT_OUTPUT_FILE_0` and increasing the number value sequentially for each subsequent file in the list. |
| `SCRIPT_HEADER_VISIBILITY` | A string that indicates a header’s visibility. If the current file is in the public or private section of the target’s Headers build phase, this string contains the value `public` or `private` to indicate its location. |
| `HEADER_OUTPUT_DIR` | The directory in which to copy header files. If the current file is in a Headers build phase, copy the file to the location in this environment variable. |

> ❗ **Important**: In your shell scripts, place environment variables in quotation marks before you pass them as parameters to other scripts or tools. The quotation marks prevent parsing errors when a variable contains spaces or special characters.

In your shell scripts, place environment variables in quotation marks before you pass them as parameters to other scripts or tools. The quotation marks prevent parsing errors when a variable contains spaces or special characters.

For a list of build setting environment variables, see [`Build settings reference`](build-settings-reference.md).

##### Specify Additional Build Dependencies for Your Source File

To improve performance during incremental builds, Xcode rebuilds only the files that require a rebuild. To determine whether a file requires a rebuild, Xcode evaluates the following criteria:

- Did the contents of the source file change?
- Does the source file depend on any other files that changed?

Xcode determines whether a source file changed by comparing the modification date of that file to the modification date of its output file. If the source file is newer, or if the output file doesn’t exist, Xcode builds the source file.

Analyzing the dependencies between source files is more complicated, but is important to ensure builds are correct. If a source file imports headers or other files, the tool that builds the source file reports the relationship to Xcode. For your custom file types, you report dependencies by generating a set of makefile rules for Xcode to execute.

To report dependency rules for your custom source files, enable the “Use discovered dependency file” option in your build rule. Xcode suggests a default naming pattern for your dependency files, but you can change the name to match your tool’s output. In your script code, create the dependency file during each build cycle, and save the file with the appropriate name.

Create the actual files in your script code when you build custom files. Fill the contents of each dependencies file with a set of makefile rules. The Xcode build system analyzes these rules at build time to determine whether it needs to rebuild the matching source file.

## See Also

- [Customizing the build schemes for a project](customizing-the-build-schemes-for-a-project.md)
  Specify which targets to build, and customize the settings Xcode uses to build, run, test, and profile those targets.
- [Customizing the build phases of a target](customizing-the-build-phases-of-a-target.md)
  Specify the tasks to perform during a build, including the source files to compile, the scripts to run, and the resources to include in the final product.
- [Running custom scripts during a build](running-custom-scripts-during-a-build.md)
  Execute custom shell scripts during the build process, and run tools or other commands that your project requires.
- [Running code on a specific platform or OS version](running-code-on-a-specific-version.md)
  Add conditional compilation markers around code that requires a particular family of devices or minimum operating system version to run.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-build-rules-for-custom-file-types)*