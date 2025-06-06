# Creating a workflow that builds your app for distribution

**Framework**: Xcode

Configure a workflow to build and sign your app for distribution to testers with TestFlight, in the App Store, or as a notarized app.

#### Overview

Delivering a version of your app to testers with TestFlight, uploading a version that’s eligible for app review, or sharing a notarized version a recipient can trust are key tasks of a continuous deployment (CD) practice. Configure an Xcode Cloud workflow that does multiple tasks, or create separate workflows — depending on your preferences, requirements, and the resulting workflow strategy.

If you’re new to continuous integration and delivery (CI/CD), see [`About continuous integration and delivery with Xcode Cloud`](about-continuous-integration-and-delivery-with-xcode-cloud.md). For more information on developing a workflow strategy, see [`Developing a workflow strategy for Xcode Cloud`](developing-a-workflow-strategy-for-xcode-cloud.md).

##### Configure the Workflow

When you create a new workflow to create a new version of your app for distribution to testers with TestFlight, in the App Store, or with notarization, make sure to:

- Restrict editing in the General settings of the workflow. This is a required step if you want to create a build that’s eligible for app review or notarization.
- In the Environments settings of the workflow, select Clean to configure the workflow so it starts builds without cached data. For more information, see [`Perform a clean build`](xcode-cloud-workflow-reference#Perform-a-clean-build.md).
- Configure an archive action for each applicable platform you want to include in this workflow. For example, add two archive actions — one for iOS and one for macOS — if you want to distribute the iOS and the macOS version of your app with one workflow.
- Choose TestFlight (Internal Testing Only) in the settings for the archive action if you want to distribute a development version to your team members with TestFlight.
- Choose TestFlight and App Store in the settings for the archive action if you want to create an app binary that’s eligible for public testing with TestFlight and for release on the App Store. Note that external testing is subject to beta app review, and similarly you need to submit your app for review before you can release it on the App Store.
- Review whether your new workflow includes test actions. If you use a separate workflow to run comprehensive tests, you may not want to configure a test action. If other workflows don’t run comprehensive tests, consider configuring a test action that performs comprehensive verifications.
- Choose start conditions that make sense for your app testing and release process. Common start conditions are branch changes to a release branch or creation of a Git tag that starts with `release`. If you want to start a build for the workflow manually, configure a start condition that never actually starts a build.
- Add a post-action for internal or external testing with TestFlight. If you choose external testing, you can later decide to submit the version for app review using App Store Connect.
- In the post-action you add, add individual testers or groups of testers in TestFlight. The people or groups you add receive the update on their test device.
- Add a post-action to notarize a macOS app if you intend to distribute it through your own channels. This sends the archive to the notary service to generate a ticket and staples the ticket to the archive. For more information, see [`Notarizing macOS software before distribution`](https://developer.apple.com/documentation/Security/notarizing-macos-software-before-distribution).
- Download and archive build artifacts after a completed build as described in [`Download and archive build artifacts`](configuring-your-first-xcode-cloud-workflow#Download-and-archive-build-artifacts.md).

When Xcode Cloud successfully builds your app and makes it available to testers in TestFlight, and you configured the workflow to create a binary that’s available for submission to app review, follow the necessary steps to release an app. For more information on using App Store Connect and TestFlight and on publishing your app in the App Store, see [`App Store Connect Help`](https://developer.apple.comhttps://developer.apple.com/help/app-store-connect/).

If your workflow includes a post-action that notarizes your app, you can download the notarized version from the artifacts of a successful build action. Navigate to the build action’s Artifacts, then select the app to download.

## See Also

- [Developing a workflow strategy for Xcode Cloud](developing-a-workflow-strategy-for-xcode-cloud.md)
  Review how you can best create custom Xcode Cloud workflows to refine your continuous integration and delivery practice.
- [Xcode Cloud workflow reference](xcode-cloud-workflow-reference.md)
  Configure metadata, start conditions, actions, post-actions, and more to create custom Xcode Cloud workflows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/creating-a-workflow-that-builds-your-app-for-distribution)*