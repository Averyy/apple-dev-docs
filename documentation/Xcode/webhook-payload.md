# Xcode Cloud webhook payload reference

**Framework**: Xcode

Review details of the webhook payload that Xcode Cloud sends, including the product, workflow, build, actions, results, and SCM metadata associated with it.

##### Webhook

##### Webhookmetadata

##### App

##### Ciworkflow

##### Ciproduct

##### Cibuilds

 - The `git` commit and SCM details for the build.

 - Optional commit details of the target commit associated with the build.

##### Cibuildactions

Information and metadata for each build action that runs as part of the build.

##### Scmprovider

##### Scmrepository

##### Scmpullrequest

##### Scmgitreference

## See Also

- [Configuring webhooks in Xcode Cloud](configuring-webhooks-in-xcode-cloud.md)
  Configure webhooks that connect Xcode Cloud to other services and tools.
- [Connecting Xcode Cloud to Slack](connecting-xcode-cloud-to-slack.md)
  Connect Xcode Cloud to Slack to keep your team informed about the latest Xcode Cloud builds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/webhook-payload)*