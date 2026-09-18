# Updating your Xcode project configuration file format

**Framework**: Xcode

Configure your Xcode project to use the JSON project configuration file format that’s more human-readable and editable by coding intelligence agents.

**Availability**:
- Xcode 27.2+ (Beta)

#### Overview

An Xcode project file with a `.xcodeproj` extension contains a project configuration file along with other files specific to your project. In previous Xcode releases, a project configuration file is a property list file with a `.pbxproj` extension. In Xcode 27.2 and later, the default project configuration file is a smaller, hierarchical, self-describing JSON file with a `.xcproj` extension. Xcode 27 and later supports both file formats so you can choose the format you prefer. For projects you created using earlier releases, you can switch to the new JSON file format.

The open source JSON file format makes verifying project configuration changes easier when committing the project configuration file to your source code repository because changes in the comparison view correspond to your actions in Xcode. Additionally, merge conflicts are less likely because the JSON file format isolates configuration changes. The JSON file format also makes it easier for coding intelligence agents to edit the file for you.

For more information on creating projects, see [`Creating an Xcode project for an app`](creating-an-xcode-project-for-an-app.md). For more information on using agents, see [`Writing code with intelligence in Xcode`](writing-code-with-intelligence-in-xcode.md).

> **Note**: The JSON file format `.xcproj` is compatible with Xcode 27 and later.

#### Change the Project Configuration File Format to Json

In the Project navigator, select the project, and in the File inspector, choose JSON from the Project Format pop-up menu under Project Document. If a dialog appears, click Continue to change the format.

The project configuration file inside the Xcode project (`.xcodeproj`), changes from a property list file with a `.pbxproj` extension to a JSON file with a `.xcproj` extension.

If you use source control, you can undo the file format change by discarding changes to individual files in the Xcode project folder (removal of the file with a `.pbxproj` and addition of the file with a `.xcproj` extension).

## See Also

- [Extending and customizing agents](extending-and-customizing-agents.md)
  Expand agent capabilities for your specific needs and application domain.
- [Giving external agents access to Xcode](giving-external-agents-access-to-xcode.md)
  Let agents access your project and Xcode capabilities using the Model Context Protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/updating-your-xcode-project-configuration-file-format)*