# Organizing your code changes with source control

**Framework**: Xcode

Use Git branches and tags to streamline your collaboration and manage features and releases.

#### Overview

If you need to keep track of multiple feature and release timelines simultaneously, you can organize different versions of your code into branches and annotate your significant changes or milestones with tags.

![Conceptual diagram that shows three rows of commits, each row representing a branch. Each commit in the topmost branch contains a tag that associates the commit with a release version number.](/images/com.apple.Xcode/organizing-your-code-changes-with-source-control-1@2x.png)

##### Organize New Feature or Bug Fix Changes in a Branch

When you update source code to add a new feature or to fix a bug, keep all the changes together in a branch so that you can work with them as a unit. For example, if you develop a feature on a separate branch and later decide to delay it, don’t merge it into your release branch.

Before you begin new work, choose a starting point for your branch. To see a list of existing branches and remote repositories, click the Repositories tab in the Source Control navigator, expand your repository, and expand the Branches and Remotes subfolders.

By default, Xcode creates a branch named *main* when you create a new project with a Git repository. Control-click the branch you want to use as your starting point, choose “Branch from [*branch name*]”, and then enter a name for your branch that identifies the work you’re doing. When you click Create, Xcode creates the branch and makes it current, so any changes you commit and push are part of that branch.

Continue making code changes, and periodically test, stage, commit, and push your changes to the branch. When your new feature or bug fix is complete and you’re ready to include your work in the main branch, review and merge it. For more information, see [`Combining code changes in a source control repository`](combining-code-changes-in-a-source-control-repository.md).

> 💡 **Tip**: You can create a new branch from the current branch with uncommitted changes, and your changes become part of the new branch. You can’t switch to another branch if you have uncommitted changes, so commit your changes or stash them before switching to another branch.

##### Set Aside Work in Progress to Make Other Changes

When you have work in progress that you aren’t ready to commit and you need to switch to another branch, stash your changes to save them without committing them to the repository. Choose Integrate > Stash Changes, and optionally enter a description of your changes.

![A screenshot of the Xcode Stash Changes dialog.](/images/com.apple.Xcode/organizing-your-code-changes-with-source-control-2@2x.png)

Xcode creates a stash entry with your changes and removes those changes from the current working project so that you can switch branches or start working on other changes.

To view your stashed changes, click the Repositories tab in the Source Control navigator, expand your repository, and then expand the Stashed Changes folder. Select a stashed change item to review the changes in the comparison view.

To add the changes to your current work, Control-click the stashed change item and choose Apply Stashed Changes. Xcode updates the current working project with the stashed changes so you can continue making updates or commit your changes to the repository.

When you no longer need the stashed changes, Control-click the stashed change item and choose Delete to remove it.

##### Mark Releases and Significant Milestones

Add tags to commits that represent a significant milestone, like a release or large feature addition, to make them easy to find in the source control history.

To find a branch or commit to tag, click the Repositories tab in the Source Control navigator, expand your repository, and then expand the Branches folder. Control-click either a branch or a branch commit, and choose Tag “[*branch name*]” or Tag “[*commit-hash*]” from the pop-up menu.

![A screenshot of the Xcode dialog for creating a new tag from a commit.](/images/com.apple.Xcode/organizing-your-code-changes-with-source-control-3@2x.png)

If you select the branch, Xcode applies the tag to the most recent commit in the branch. Enter a short string for the tag, and, optionally, a more detailed message. Click Create, and Xcode creates the tag and marks the commit with it.

To view the commits that you tag, click Repositories in the Source Control navigator and expand the Tags folder. Xcode shows a list of commits with tags in the detail area. Use the tabs and Filter field above the list to limit or expand the commits.

## See Also

- [Combining code changes in a source control repository](combining-code-changes-in-a-source-control-repository.md)
  Integrate code changes from multiple sources and resolve conflicts between different versions of code using source control tools in Xcode.
- [Configuring source control in Xcode](configuring-source-control-in-xcode.md)
  Customize the default Xcode Settings for connecting to Git repositories, applying code changes, and more options for configuring source control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/organizing-your-code-changes-with-source-control)*