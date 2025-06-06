# Combining code changes in a source control repository

**Framework**: Xcode

Integrate code changes from multiple sources and resolve conflicts between different versions of code using source control tools in Xcode.

#### Overview

If you use source control to work on code with collaborators or to manage multiple versions of your Xcode project for different releases, eventually, you need to sync code changes between versions. Git source control provides a mechanism for combining sets of code changes by merging those changes together, and Xcode provides a visual interface for performing a .

![Conceptual diagram that shows two rows of commits, each row representing a branch. The rightmost commit in the bottom row merges into the top row to illustrate two commits merging together.](https://docs-assets.developer.apple.com/published/357f965f3904cf401c393b515a8084dd/combining-code-changes-in-a-source-control-repository-1%402x.png)

##### Merge Code Changes

After you complete work in a feature or bug fix branch, you merge your changes into your main development or production branch. Alternatively, you merge other updates from your main development or production branch into your feature or bug fix branch to resolve conflicts or to sync your work with the latest updates and ensure everything functions appropriately before merging back into your main development or production branch.

1. Open the Source Control navigator.
2. In the Repositories navigator, expand your repository and the Branches folder.
3. Select the branch you want to merge into, and then Control-click and choose Switch to make that branch the current branch.
4. Select the branch you want to merge from, and then Control-click and choose “Merge [] into []”.

If there are no conflicts, Xcode completes the merge.

##### Resolve Conflicts with Other Code

In a source control repository, a  occurs when two commits have incompatible changes and Git can’t merge the changes automatically. For example, a conflict might occur when two developers change the same lines in the same source file.

When you attempt to merge changes in Xcode, if there are conflicts, Xcode presents a comparison view for you to review and resolve the conflicts.

![The Xcode merge conflict view showing a list of files to merge and highlighting the file with a conflict. The view shows the conflict and the button you use to select a resolution for it. The view also highlights the buttons to navigate between conflicts in a file.](https://docs-assets.developer.apple.com/published/ebd9e5af50ccc49e115840f991ed6f82/combining-code-changes-in-a-source-control-repository-2%402x.png)

To resolve a conflict, click the numbered change for that conflict and select which option you want to use to resolve it:

- Choose Left
- Choose Right
- Choose Left Then Right
- Choose Right Then Left

After you choose a resolution for each conflict, Xcode enables the Merge button. Click the Merge button to complete the merge, or click Cancel to abort the merge and restore your branch so you can make more changes before merging.

## See Also

- [Organizing your code changes with source control](organizing-your-code-changes-with-source-control.md)
  Streamline your collaboration workflow by managing your Xcode project’s features and releases with Git branches and tags.
- [Configuring source control preferences in Xcode](configuring-source-control-preferences-in-xcode.md)
  Customize the default Xcode Settings for connecting to Git repositories, applying code changes, and more options for configuring source control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/combining-code-changes-in-a-source-control-repository)*