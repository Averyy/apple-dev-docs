# Xcode Cloud workflow reference

**Framework**: Xcode

Configure metadata, start conditions, actions, post-actions, and more to create custom Xcode Cloud workflows.

#### Overview

By configuring a first workflow in Xcode, you started a continuous integration and delivery (CI/CD) practice with Xcode Cloud. After you’ve reviewed how you can best refine your CI/CD practice as described in [`Developing a workflow strategy for Xcode Cloud`](developing-a-workflow-strategy-for-xcode-cloud.md), create custom workflows that fit the unique needs for ensuring your app’s or framework’s quality. For example, add metadata to describe the purpose of a workflow, configure conditions that start a new build, add actions and post-actions, and more.

You need to use Xcode to initially configure your project or workspace to use Xcode Cloud. However, after you’ve started your first build, you can edit and create workflows in either Xcode or [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com).

For additional information about Xcode Cloud workflows, see [`Explore Xcode Cloud workflows`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10268) and [`Customize your advanced Xcode Cloud workflows`](https://developer.apple.comhttps://developer.apple.com/wwdc21/10269).

##### Metadata

Even if you’re a solo developer, you might create several workflows. To help distinguish workflows from each other and make each workflow’s purpose easy to understand, open the workflow and provide metadata in the General section.

![A screenshot that shows a workflow in Xcode. The General section is visible and shows the name and description that the user provided.](https://docs-assets.developer.apple.com/published/f5090090ba3a21cc016c980e101019cd/Xcode-Cloud-Workflow-Reference-1%402x.png)

##### Environment

When you develop and maintain your app or framework over time, you need to make sure that current and upcoming Xcode versions can successfully build it. If your product is a framework, you might need to ensure your framework supports previous Xcode versions.

> ❗ **Important**: Periodically, Xcode Cloud may update available macOS and Xcode versions and subsequently ask you to update your workflows for them to continue to build successfully.

Periodically, Xcode Cloud may update available macOS and Xcode versions and subsequently ask you to update your workflows for them to continue to build successfully.

To reduce the work needed to perform these verifications, configure a workflow’s temporary build environment. For example, create a workflow that builds your project and runs your tests using the latest publicly released Xcode and macOS versions. Then, create another workflow that performs the same verifications with the latest beta versions of macOS and Xcode.

To configure a workflow’s temporary build environment, navigate to the workflow’s Environment section, and choose from available Xcode and macOS versions.

> **Note**: The temporary build environment that Xcode Cloud uses includes tools that are part of macOS and Xcode — for example, Python — and additionally [`Homebrew`](https://developer.apple.comhttps://brew.sh) to support installing third-party dependencies and tools. For more information, see [`Making dependencies available to Xcode Cloud`](making-dependencies-available-to-xcode-cloud.md).

The temporary build environment that Xcode Cloud uses includes tools that are part of macOS and Xcode — for example, Python — and additionally [`Homebrew`](https://developer.apple.comhttps://brew.sh) to support installing third-party dependencies and tools. For more information, see [`Making dependencies available to Xcode Cloud`](making-dependencies-available-to-xcode-cloud.md).

##### Perform a Clean Build

To reduce the amount of time it takes to perform a build, Xcode Cloud stores each build’s derived data and other cached information for reuse in a secure and private way. However, you might need to perform a clean build that doesn’t cache data. For example, you need to configure a workflow to perform a clean build if you add a post-action that distributes a new version to external testers with [`TestFlight`](https://developer.apple.comhttps://developer.apple.com/testflight/).

To configure a workflow that starts a new build without cached data:

1. Open the workflow in Xcode or App Store Connect and navigate to the Environment section.
2. Select Clean and save the workflow.

> **Note**: Enabling clean builds significantly increases the time it takes to perform a build. Only perform clean builds when necessary; for example, distributing a new version to external testers with TestFlight requires a clean build.

Enabling clean builds significantly increases the time it takes to perform a build. Only perform clean builds when necessary; for example, distributing a new version to external testers with TestFlight requires a clean build.

##### Custom Environment Variables

In addition to Xcode and macOS versions, you can set custom  for a workflow in its Environment section. These variables are available to custom build scripts you use to extend workflows. For example, set a secret environment variable to contain an API key you use in a custom build script that uploads a workflow’s artifacts to your server.

> ❗ **Important**: To securely store an environment variable and make sure it doesn’t appear in any logs, check the “Keep value redacted” (Xcode) or Secret (App Store Connect) box.

To securely store an environment variable and make sure it doesn’t appear in any logs, check the “Keep value redacted” (Xcode) or Secret (App Store Connect) box.

##### Start Conditions

When you create a new workflow, Xcode suggests the Branch Changes condition that starts a new build for every change to your Git repository’s default branch. This condition is useful when you get started with CI. However, starting a build for every change to your default branch might not be the appropriate setting for you. For example, a workflow that runs UI tests on many simulated devices can take a significant amount of time to complete, and starting a build for every branch change isn’t practical. In this case, make changes to the workflow’s start condition or add start conditions to tell Xcode Cloud to perform a workflow less often.

For more information about configuring start conditions, see [`Configuring start conditions`](configuring-start-conditions.md).

##### Auto Cancel Builds

By default, workflows have the Auto-cancel Builds setting enabled for each start condition. As a result, Xcode Cloud automatically cancels an in-progress build if a workflow queues a new build for the same workflow. This reduces the time to verify your latest code change — a useful setting in case you push updates to a branch in quick succession.

For example, say you push five changes to a branch within five minutes. Xcode Cloud detects each change and starts a build because it meets the Branch Changes start condition, resulting in five builds. To know whether your fifth change passed the configured verifications, you’d have to wait for each build to complete, even though the fifth change supersedes the others. With Auto-cancel Builds enabled, Xcode Cloud cancels the first four builds and immediately starts the build for the latest change.

> 💡 **Tip**: If you prefer not to cancel builds automatically, turn off Auto-cancel Builds for one, multiple, or each start condition in a start condition’s Options section.

If you prefer not to cancel builds automatically, turn off Auto-cancel Builds for one, multiple, or each start condition in a start condition’s Options section.

##### Actions

Automatically and frequently building your project and verifying changes is key to a CI/CD practice. As a result, configuring a workflow’s actions is a fundamental task you perform in its Actions section. A workflow can perform the following actions:

- Build
- Test
- Analyze
- Archive

Note how these actions match your project’s or workspace’s scheme actions. To create a workflow that fits your requirements, add as many actions to a workflow as needed. For example, create a workflow that performs the test and archive actions for your app.

For detailed information on actions you configure for an Xcode Cloud workflow, see [`Configuring your Xcode Cloud workflow’s actions`](configuring-your-xcode-cloud-workflow-s-actions.md). For additional information on using Xcode Cloud to run your tests, see [`Author fast and reliable tests for Xcode Cloud`](https://developer.apple.comhttps://developer.apple.com/wwdc22/110361).

##### Post Actions

Performing actions is at the core of a workflow. However, similar to how you configure post-actions in a scheme, you can configure post-actions for a workflow that happen after Xcode Cloud performs the workflow’s actions.

By adding post-actions, you can:

- Configure custom notification settings. For example, limit email notifications to a certain build status, let Xcode Cloud email additional coworkers, or configure Xcode Cloud to send notifications to [`Slack`](https://developer.apple.comhttps://slack.com).
- Distribute a new version of your app to testers using [`TestFlight`](https://developer.apple.comhttps://developer.apple.com/testflight/).
- Upload a version of your app to App Store Connect that you can subsequently submit for app review.

For additional information on sending notifications to Slack, see [`Connecting Xcode Cloud to Slack`](connecting-xcode-cloud-to-slack.md)

##### Custom Build Scripts

Xcode Cloud uses your project’s configured schemes and offers a wide variety of workflow settings. However, you might want to perform additional custom tasks you can’t configure using a scheme or workflow. For example, you might need to install an additional tool to build your project, to upload an app archive to storage, to use a different app icon for nightly builds, and so on.

To address these use cases, you can create shell scripts, referred to as , that Xcode Cloud runs at a specific moment during a build. For more information, see [`Writing custom build scripts`](writing-custom-build-scripts.md).

##### Automate Workflow Management

Using either Xcode or App Store Connect, you can create custom workflows to verify the quality of your apps or frameworks. However, you may need to further automate Xcode Cloud usage and create and manage numerous workflows for multiple apps — especially in a corporate context. If this applies to you, use the App Store Connect API to manage workflows, start builds, and access Xcode Cloud data. For more information, see [`Xcode Cloud Workflows and Builds`](https://developer.apple.com/documentation/AppStoreConnectAPI/xcode-cloud-workflows-and-builds).

## Topics

### Start conditions
- [Configuring start conditions](configuring-start-conditions.md)
  Configure Xcode Cloud to start a build when you update a branch, pull request, or Git tag, or based on a schedule.
### Actions
- [Configuring your Xcode Cloud workflow’s actions](configuring-your-xcode-cloud-workflow-s-actions.md)
  Add actions to an Xcode Cloud workflow to build, test, analyze, and archive your app or framework when it performs a build.

## See Also

- [Developing a workflow strategy for Xcode Cloud](developing-a-workflow-strategy-for-xcode-cloud.md)
  Review how you can best create custom Xcode Cloud workflows to refine your continuous integration and delivery practice.
- [Creating a workflow that builds your app for distribution](creating-a-workflow-that-builds-your-app-for-distribution.md)
  Configure a workflow to build and sign your app for distribution to testers with TestFlight, in the App Store, or as a notarized app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/xcode-cloud-workflow-reference)*