# Reporting feedback for Xcode Cloud

**Framework**: Xcode

Provide feedback on issues you encounter when building with Xcode Cloud.

#### Overview

You can file feedback about Xcode Cloud directly from a build in the Report Navigator. When you file feedback from a build, the system prepopulates the feedback form with build-specific context that Apple can use to triage a bug.

The prepopulated information includes details describing the build as well as logs and build artifacts that may provide clues about the causes of a bug.

> ❗ **Important**: These artifacts and logs might contain personal data and intellectual property. You can opt out of providing any or all of these files before submitting feedback.

These artifacts and logs might contain personal data and intellectual property. You can opt out of providing any or all of these files before submitting feedback.

##### Initiate Feedback

To report feedback that’s not related to a specific build, select Help > Provide Feedback in Xcode or launch the Feedback Assistant app. In cases where you need to report feedback that includes build-specific context:

1. Navigate to the specific build number in the Report Navigator’s outline view.
2. Control-click on the build number to open a context menu.
3. Choose Send Feedback.

Alternatively, to issue a report from an issue banner inside a build in Xcode, click the Report Issue button.

By initiating feedback from a specific build, Xcode prepopulates the feedback form with relevant information, details describing the build (such as team name, product name, and build number) and the system-generated logs and artifacts relevant to triaging issues related to builds.

##### Review the Attachments

Text logs from commands initiated by Xcode Cloud, result bundles, and sysdiagnose logs are very useful when triaging a build-related issue. Provide these logs to help make bugs more actionable, but review the logs before you submit feedback.

To review a specific attachment, select the magnifying glass icon on the right of the item listed under Attachments. This opens Finder to the location of the attachment on disk.

At a high level, there are 5 different types of logs and build artifacts:

##### Remove Attachments and Submit Feedback

Only include attachments you want to share. To remove an attachment you don’t want to share:

1. Select the trash icon next to the item listed under Attachments.
2. To confirm the removal, select Remove from the Feedback Assistant dialog.

When the report reflects the feedback you would like to share, click the Submit button to send the feedback to Apple.

## See Also

- [Resolving common configuration and build issues](resolving-common-configuration-and-build-issues.md)
  Review common configuration and build issues and learn how you can resolve them.
- [Resolve GitHub Enterprise connection issues](resolve-github-enterprise-connection-issues.md)
  Verify that Xcode Cloud can access your GitHub Enterprise repository and fix configuration issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/reporting-feedback-for-xcode-cloud)*