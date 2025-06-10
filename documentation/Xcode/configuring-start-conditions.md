# Configuring start conditions

**Framework**: Xcode

Configure Xcode Cloud to start a build when you update a branch, pull request, or Git tag, or based on a schedule.

#### Overview

Xcode Cloud watches your Git repository for changes, checks whether a change meets start conditions you configure for your workflows, and starts a build when a change meets one of the conditions. This makes configuring start conditions a key task when you create custom Xcode Cloud workflows.

You can configure your Xcode Cloud workflow with any of the following start conditions:

By configuring several start conditions for one workflow and reusing the workflow at different moments in your development life cycle, you can reduce the number of workflows you need to maintain. For example, you can configure one workflow to perform verifications for each change to a branch or a pull request — you don’t need to configure two separate workflows.

For additional information about Xcode Cloud workflows, see [`Xcode Cloud workflow reference`](xcode-cloud-workflow-reference.md), [`Explore Xcode Cloud workflows`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10268), and [`Customize your Advanced Xcode Cloud workflows`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10269).

#### Edit Add and Remove Start Conditions

To make changes to a workflow’s start conditions, open your workflow in Xcode, choose an already configured start condition in the Start Conditions section, or add a new start condition using the Add button (+) next to Start Conditions.

![A screenshot that shows a workflow’s Start Condition section in Xcode.](https://docs-assets.developer.apple.com/published/0cebc0036f895ab33ee17b035ebf1d99/Configuring-Start-Conditions-1%402x.png)

Additionally, configure your workflow and its start conditions in the Xcode Cloud tab on the [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com) website. This is especially convenient if you manage Xcode Cloud workflows but don’t have access to the Xcode project — a common case in a corporate context.

![A screenshot that shows a workflow’s Start Condition section on the App Store Connect website.](https://docs-assets.developer.apple.com/published/3b9170566c086e631a8d7ef192e3e1fa/Configuring-Start-Conditions-2%402x.png)

> **Note**: You need to use Xcode to initially configure your project or workspace to use Xcode Cloud. After you’ve started your first build, you can manage workflows in either Xcode or App Store Connect.

##### Review the Default Start Condition

When you create a new workflow, Xcode configures a default workflow that uses the Branch Changes start condition for each change to your repository’s default branch. Even if the workflow doesn’t take a lot of time to complete, starting a new build for every change from your repository’s default branch can be impractical. For example, a workflow that runs UI tests on many simulated devices can take a significant amount of time and slow your development cycle. To start builds less frequently, use a different start condition or configure Xcode Cloud to monitor or ignore changes to specific files or folders as described in [`Monitor or ignore specific files and folders`](configuring-start-conditions#Monitor-or-ignore-specific-files-and-folders.md) below.

##### Monitor Custom Branches for Changes

By default, workflows use the Branch Changes start condition for your Git repository’s default branch. However, you might want to configure Xcode Cloud to monitor a different branch, several branches, or every branch for changes.

First, open your workflow in Xcode or App Store Connect. Select or add the Branch Changes start condition, then choose from the following settings:

- Choose the Any Branch setting to monitor every branch for changes. Note that this setting can start a lot of builds unless you set the Auto-cancel Builds setting or configure custom conditions.
- Choose the Custom Branches setting to add one or more custom branches. Existing branches appear as you type, and both Xcode and App Store Connect display a warning if you enter a branch that doesn’t exist in your remote Git repository.

![A screenshot of Xcode that shows a workflow’s Start Condition section with configured custom branches that begin with the string “feature”.](https://docs-assets.developer.apple.com/published/1255d2063c06efd43c8ff07693beb332/Configuring-Start-Conditions-3%402x.png)

> 💡 **Tip**: Instead of specifying several custom branches, configure a workflow to start a build from every branch that starts with a custom string. For example, enter `feature` and choose “Branches beginning with feature”.

You can further customize the Branch Changes start condition with the Custom Conditions setting. For more information, see [`Monitor or ignore specific files and folders`](configuring-start-conditions#Monitor-or-ignore-specific-files-and-folders.md) below.

##### Start Builds for Changes to a Pull Request

By using pull requests, you use a collaborative software development process that helps with identifying errors. To help detect issues in a PR, add the Pull Request Changes start condition to a workflow. Xcode Cloud starts a new build when you create or update a PR.

When it detects a new or updated PR, Xcode Cloud checks out the PR’s source branch — the branch that contains your changes — and the PR’s target branch. It then merges both branches in a temporary environment and performs the workflow’s configured actions.

By default, the Pull Request Changes condition starts a new build for each new or updated PR. However, you can choose from the following settings for the Pull Request Changes start condition to limit when Xcode Cloud performs the workflow:

- Configure the Source Branch setting. Choose Custom Branches and specify one or more custom branches. Xcode Cloud only performs the workflow if a pull request change involves the specified source branches.
- Configure the Target Branch setting. Choose Custom Branches to only start a build if the PR involves one or more custom target branches.

Instead of specifying several custom source and target branches, configure a workflow to start a build if a PR involves branches that start with a custom string. For example, use Any Branch for the Source Branch setting. Then, change the Target Branch setting to Custom Branches and enter `release`. As a result, Xcode Cloud starts a build from every PR that targets branches that start with  `release`.

![A screenshot of Xcode that shows a workflow that uses the Pull Request Changes start condition. The user has configured the condition to start a new build for PRs for any source branch and target branches that start with the string release.](https://docs-assets.developer.apple.com/published/947882645f31327e222f1a91ffce6e24/Configuring-Start-Conditions-4%402x.png)

You can further customize the Pull Request Changes start condition with the Custom Conditions setting. For more information, see [`Monitor or ignore specific files and folders`](configuring-start-conditions#Monitor-or-ignore-specific-files-and-folders.md) below.

##### Start Builds for New or Updated Git Tags

Similar to how you can configure a workflow that starts a new build if a branch changes, configure Xcode Cloud to start a build if you create or update a Git tag. Add the Tag Changes start condition in Xcode or App Store Connect to a workflow and choose between:

![A screenshot of App Store Connect that shows the Tag Changes start condition. The user has configured the condition for tags that start with the string v1.](https://docs-assets.developer.apple.com/published/8abef81abe384ea68521d8d2c19a0204/Configuring-Start-Conditions-5%402x.png)

> 💡 **Tip**: Instead of specifying several custom tags, configure a workflow to start a build from every tag that starts with a given string. For example, enter `v1` and choose “Tags beginning with v1”.

You can further customize the Branch Changes start condition with the Custom Conditions setting.

##### Monitor or Ignore Specific Files and Folders

If you add the Branch Changes, Pull Request Changes, or Tag Changes start condition to a workflow, there’s a chance Xcode Cloud starts new builds too often. For example, your team may use a single repository for all of your team’s code and not every change affects your app. In contrast, you might want Xcode Cloud to only start a build if a specific file or folder changes. To accommodate these use cases, further configure start conditions to ignore changes to custom files and folders or to only start a build if a specified file or folder changes.

First, open a workflow in Xcode or App Store Connect and select a start condition. Change the Files and Folders setting to Custom Conditions. Then, add one or more custom conditions to tell Xcode Cloud to ignore changes to specific files and folders, or to start a build in response to changes to specific files or folders.

You can configure a custom condition to either start or skip a build if:

- Any file in any folder or a custom folder changes.
- A specific file in any folder or in a custom folder changes.
- Files with a provided file extension in any folder or in a custom folder change.

For example:

- Choose Start a Build, choose Any File, then choose a folder to start a build if the contents of the selected folder change.
- Choose Don’t Start a Build, choose Filename, enter a filename, and then choose any folder to configure a workflow to not start a build for any files that match the name.
- Choose Start a Build, choose File Extension, enter a file extension, and then choose a folder to start a build if files with the entered file extension change.

If you choose Filename, don’t include a wildcard like `*` in the filename. For example, don’t enter `Release-Notes-*.md`. If you tell Xcode Cloud to monitor a specific folder for changes, it recursively monitors files contained in the given folder. For example, if you organize your code in a `Source` folder and tell Xcode Cloud to monitor it for changes, changes to files in `Source/iOS` start a new Xcode Cloud build.

> **Note**: A start condition’s Custom Conditions setting can either start or skip a build, not both.

##### Skip a Build

When you push changes to your Git repository in quick succession — for example, in early development of your app — you may want Xcode Cloud to ignore a change and not start a build. To tell Xcode Cloud to skip a build when you push changes, include `[ci skip]` in the title or message of the latest commit you push to your remote repository.

If you require Xcode Cloud builds or actions to succeed before users can merge a PR, the website for a PR indicates that Xcode Cloud skipped a build for the most recent change. To learn more about configuring requirements for PRs, see [`Configuring requirements for merging a pull request`](configuring-requirements-for-merging-a-pull-request.md).

##### Set a Schedule

In addition to starting a build when a change meets a start condition, you can configure a workflow to start a build based on a schedule. For example, distributing a new version of your app to testers with [`TestFlight`](https://developer.apple.comhttps://developer.apple.com/testflight/) for every branch or pull request change will overwhelm your testers. Instead, distribute a new version based on a schedule; for example, once per week.

To configure a workflow to start a build based on a schedule, add the On a Schedule for a Branch start condition and specify the frequency, time, and branch.

The following screenshot shows a workflow that starts a build on every business day at 10:00 p.m. Central European Time from the `main` branch:

![A screenshot that shows a workflow in Xcode that starts a build on every business day at 10:00 p.m. Central European Time from the main branch.](https://docs-assets.developer.apple.com/published/1ff44dae3cd867ac936204e92fd949ab/Configuring-Start-Conditions-6%402x.png)

##### Manually Start a Build

Team members can manually start an Xcode Cloud build for workflows you configure with specific start conditions. To support starting a build manually without tying it to a Git event or a schedule, add a Manual Start condition and configure the specific branches, tags, and pull requests to which it applies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-start-conditions)*