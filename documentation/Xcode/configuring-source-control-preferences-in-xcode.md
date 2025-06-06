# Configuring source control preferences in Xcode

**Framework**: Xcode

Customize the default Xcode Settings for connecting to Git repositories, applying code changes, and more options for configuring source control.

#### Overview

Xcode lets you customize many default options for working with source control repositories. To modify the default source control preferences, choose Xcode > Settings > Source Control.

##### Enable Source Control Actions

In the General tab of Source Control settings, select the Enable Source Control option to enable the actions in the Source Control menu and the Source Control navigator. Enabling source control also displays the Git tab, which you use to configure Git integration options.

![The Xcode Settings dialog showing the Source Control preference pane with the General tab in a selected state. The Enable Source Control option and each of its suboptions are enabled. The Show Source Control changes option is also enabled.](https://docs-assets.developer.apple.com/published/ac86f51093b66bdb9259d6f96007054f/configuring-source-control-preferences-in-xcode-1%402x.png)

##### Choose Automatic Source Control Behavior

After you enable source control, you can select additional options to specify which source control tasks you want Xcode to perform for you automatically.

- Refresh local status automatically: Xcode automatically refreshes the status of source control managed files when they change.
- Fetch and refresh server status automatically: For remote repositories, Xcode periodically refreshes the status of files that update on the server. (To manually refresh the status, choose Source Control > Fetch and Refresh Status.)
- Add and remove files automatically: Xcode automatically updates working copies when adding or removing files in your projects.
- Select files to commit automatically: Xcode automatically selects which files to stage for a commit.

##### Show Code Changes in the Source Editor

The Text Editing settings affect whether Xcode indicates code changes in the source editor.

- Show Source Control changes: Xcode shows the change bar, next to the lines that changed, in the gutter of the source editor.
- Include upstream changes: Xcode shows the changes committed by others (that may conflict with your edits) in the source editor gutter.

##### Customize the Comparison View Layout

The Comparison View setting specifies where the local version of the code appears in the version editor. To show the local version on the left, choose “Local Revision on Left Side” from the pop-up menu; otherwise, choose “Local Revision on Right Side.”

##### Choose Sorting Options for the Source Control Navigator

The Source Control Navigator setting specifies how Xcode sorts the files in the Source Control navigator. To sort by name, choose “Sort by Name” from the pop-up menu; otherwise, choose “Sort by Date.”

##### Customize Git Settings

In the Git tab, you can configure default settings for Git repositories that you manage through Xcode.

![The Xcode Settings dialog showing the Source Control preference pane with the Git tab in a selected state. The Author Name, Author Email, and Ignored Files fields contain example values.](https://docs-assets.developer.apple.com/published/385c8d57207cfbe73a7dc60eafa1fa40/configuring-source-control-preferences-in-xcode-2%402x.png)

Customize the Author Name and Author Email to use in the source control history. Users can Control-click a history entry to email the author.

Use the Ignored Files list to specify the files that you don’t want Git to commit to your source control repositories. To add an ignored file, click the Add button (+). To remove an ignored type, select an item in the list, then click the Delete button (–). To edit an item, double-click it.

Choose additional options for handling Git commands:

- Prefer to rebase when pulling: Perform a Git rebase when pulling changes instead of a merge.
- Show merge commits in per-file log: Show Git merge commits in the project history.

## See Also

- [Organizing your code changes with source control](organizing-your-code-changes-with-source-control.md)
  Streamline your collaboration workflow by managing your Xcode project’s features and releases with Git branches and tags.
- [Combining code changes in a source control repository](combining-code-changes-in-a-source-control-repository.md)
  Integrate code changes from multiple sources and resolve conflicts between different versions of code using source control tools in Xcode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-source-control-preferences-in-xcode)*