# Configuring source control in Xcode

**Framework**: Xcode

Customize the default Xcode Settings for connecting to Git repositories, applying code changes, and more options for configuring source control.

#### Overview

Xcode lets you customize many default options for working with source control repositories. To modify the default source control settings, choose Xcode > Settings and click Source Control in the sidebar.

##### Enable Source Control Actions

In the Source Control settings, select the “Enable source control” option to enable the actions in the Integrate menu and the Source Control navigator. Enabling source control also enables the “Git settings” option under Settings, which you use to configure Git integration options.

![The Xcode Settings dialog showing the Source Control settings. The Enable Source Control option and each of its suboptions are selected. The Show Source Control changes option is also selected.](https://docs-assets.developer.apple.com/published/9130d1d8ccd9832a518f6bd28e73e512/configuring-source-control-in-xcode-1%402x.png)

##### Choose Automatic Source Control Behavior

After you enable source control, you can select additional options to specify which source control tasks you want Xcode to perform for you automatically.

- Refresh local status automatically: Xcode automatically refreshes the status of source control managed files when they change.
- Fetch and refresh server status automatically: When using remote repositories, Xcode periodically refreshes the status of files that update on the server. (To manually refresh the status, choose Integrate > Fetch Changes and Refresh File Status.)
- Add and remove files automatically: Xcode automatically updates working copies when adding or removing files in your projects.

##### Show Code Changes in the Source Editor

The text editing settings affect whether Xcode indicates code changes in the source editor.

- Show source control changes: Xcode shows the change bar, next to the lines that changed, in the gutter of the source editor.
- Include upstream changes: Xcode shows the changes committed by others (that may conflict with your edits) in the source editor gutter.

##### Customize the Comparison View Layout

The comparison view setting specifies where the local version of the code appears in the version editor. To show the local version on the left, choose “Local Revision on Left Side” from the pop-up menu; otherwise, choose “Local Revision on Right Side.”

##### Choose Sorting Options for the Source Control Navigator

The Source Control navigator setting specifies how Xcode sorts the files in the Source Control navigator. To sort by name, choose Sort by Name from the pop-up menu; otherwise, choose Sort by Date.

##### Customize Git Settings

To configure default settings for Git repositories that you manage through Xcode, click “Git settings.”

![The Xcode Settings dialog showing the Source Control > Git Settings selected. The Author name and Author email fields contain example values.](https://docs-assets.developer.apple.com/published/584916c321c7716f1f32acece10603ef/configuring-source-control-in-xcode-2%402x.png)

Customize the Author Name and Author Email to use in the source control history. Users can Control-click a history entry to email the author.

Choose additional options for handling Git commands:

- Prefer to rebase when pulling: Perform a Git rebase when pulling changes instead of a merge.
- Show merge commits in per-file log: Show Git merge commits in the project history.

Use the Ignored Files list to specify the files that you don’t want Git to commit to your source control repositories.

- To add an ignored file, click the Add button (+).
- To remove an ignored type, select an item in the list, then click the Delete button (–).
- To edit an item, double-click it.

## See Also

- [Organizing your code changes with source control](organizing-your-code-changes-with-source-control.md)
  Use Git branches and tags to streamline your collaboration and manage features and releases.
- [Combining code changes in a source control repository](combining-code-changes-in-a-source-control-repository.md)
  Integrate code changes from multiple sources and resolve conflicts between different versions of code using source control tools in Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-source-control-in-xcode)*