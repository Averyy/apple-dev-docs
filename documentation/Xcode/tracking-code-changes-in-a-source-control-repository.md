# Tracking code changes in a source control repository

**Framework**: Xcode

Create a history of incremental code changes to your Xcode project’s source control repository with Git commits.

#### Overview

When you use a source control repository to manage your Xcode project, you save changes to your repository in incremental states called commits. A  consists of a snapshot of your project’s state at a particular point in time, a message that describes the set of changes from the previous commit, and additional metadata like a unique hash that identifies the commit.

![Conceptual diagram that shows one row of four commits. The rightmost commit contains a label that describes some information about the commit, including a commit hash, commit message, and author name.](https://docs-assets.developer.apple.com/published/e531630d352ad4ce907bcbff40ded594/tracking-code-changes-in-a-source-control-repository-1%402x.png)

In Xcode, you can save your project’s current state in a commit, navigate the history of your project’s previous commits, compare changes between specific commits, and quickly restore to a previous commit.

##### Save Your Projects Current State

As you make changes to your source code in a source control repository, Xcode tracks those changes and highlights them in the Project navigator and in the source editor. While you’re working on a change, look at the Project navigator to see your changes in the current branch.

![The Xcode Project navigator showing a modified file and a new file. The source code editor shows a change indicator that displays the old code and new code.](https://docs-assets.developer.apple.com/published/4e2c11212723f1a6b809356cc2348918/tracking-code-changes-in-a-source-control-repository-2%402x.png)

The Project navigator annotates files with changes since the last commit, using an  for new files or an  for modified files. To compare changes in one source file, open the file and click the Enable Code Review button in the upper-right corner of the Xcode window.

![The Xcode comparison view showing changes between the current local version on the left and the most recent source-control commit on the right. The view shows a highlighted change, a numbered change, where to select branches and commits on each side of the view, and where to click buttons to navigate between commits.](https://docs-assets.developer.apple.com/published/5ddb1d8f119ec7aa18a6077868633902/tracking-code-changes-in-a-source-control-repository-3%402x.png)

The comparison view highlights changes between the current source code and the most recent commit. You can choose whether to view changes inline or side by side by clicking the Adjust Editor Options button.

The comparison view allows you to:

- Navigate between the numbered changes using the arrows at the bottom of the center column.
- Click a number in the center column to select and discard a change.
- Choose other commits to compare your current changes against.

When you’re done making changes, commit them to save them permanently in your source control repository. Choose Source Control > Commit, and review your changes.

![The Xcode commit view showing a list of files with changes. The comparison view shows a highlighted change in an updated source file. The commit message area has an example commit message.](https://docs-assets.developer.apple.com/published/911912557e732f90ac022f91bf536607/tracking-code-changes-in-a-source-control-repository-4%402x.png)

In the Project navigator, select a file in the list to view the code changes for that file. Click the numbered selector between the left and right sides of the comparison view, and then choose Don’t Commit to exclude an individual change from your commit, or choose Discard Change to remove a change. Select checkmarks to indicate which files to include in your commit.

> ⚠️ **Warning**: When you add a new file or delete an unused file, you must commit both the file and the Xcode project file (called `project.pbxproj`) together for your project to remain in a consistent state.

When you add a new file or delete an unused file, you must commit both the file and the Xcode project file (called `project.pbxproj`) together for your project to remain in a consistent state.

Document your changes with a commit message that describes what your commit accomplishes. Click the “Commit [] files” button to commit your changes, or click Cancel to continue working without committing to the repository. Xcode shows the commit message you provide when you look at the source control history.

If you don’t want to commit any of your changes, and want to remove them, choose Source Control > Discard All Changes, and click Discard. Xcode removes all the current changes and restores your source files to the most recent commit.

##### View a History of Project States

Xcode has a commit history view that lets you view historical changes for your source control repository when you’re investigating a bug or adding code for a new feature.

1. Open the Source Control navigator.
2. In the Repositories navigator, expand your repository and the Branches folder.
3. Select a branch to display a list of commits.
4. Double-click a specific commit to display the comparison view, and see additional information about the commit in the Source Control inspector.

![The Xcode commit history view showing a list of commits. The bottom commit is in a selected state.](https://docs-assets.developer.apple.com/published/332208568f78d1ddb6921184a17fc90b/tracking-code-changes-in-a-source-control-repository-5%402x.png)

##### Compare Code Between Specific Project States

To compare code between specific commits, select the branches and commits to compare from the bottom bar in the comparison view.

![The Xcode comparison view showing highlighted changes in a comparison between two specific commits.](https://docs-assets.developer.apple.com/published/d181f9aab04e2a4f03cfcdf7125dd378/tracking-code-changes-in-a-source-control-repository-6%402x.png)

##### Restore Your Project to a Previous State

You can quickly restore your code to a previous state in your source control repository by checking out a specific commit. Xcode restores your project files to the state that the commit you choose specifies.

Before you restore a previous commit of the code, make sure you don’t have any uncommitted changes. If you do, you can either discard the changes (Source Control > Discard All Changes) or save them to apply later by stashing them (Source Control > Stash Changes).

1. Open the Source Control navigator.
2. In the Repositories navigator, expand your repository and the Branches folder.
3. Select the branch that contains the commit you want to restore.
4. In the detail view, Control-click the desired commit and choose Switch to “[]”.
5. In the confirmation dialog, click Switch. Xcode restores your project’s state to the earlier commit.

To learn more about restoring stashed changes, see [`Organizing your code changes with source control`](organizing-your-code-changes-with-source-control.md).

## See Also

- [Configuring your Xcode project to use source control](configuring-your-xcode-project-to-use-source-control.md)
  Sync code changes between team members and development computers by setting up your Xcode project to use Git source control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/tracking-code-changes-in-a-source-control-repository)*