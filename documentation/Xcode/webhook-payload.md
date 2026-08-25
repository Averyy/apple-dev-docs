# Xcode Cloud webhook payload reference

**Framework**: Xcode

Review details of the webhook payload that Xcode Cloud sends, including the product, workflow, build, actions, results, and SCM metadata associated with it.

##### Webhook

- **`id`**: A string that uniquely identifies the webhook, such as `12345678-abcd-1234-5678-a12345bc4567`.
- **`name`**: The name of the webhook, such as `Team Dashboard`.
- **`url`**: The URL of the app or service that receives and handles the webhook.

##### Webhookmetadata

- **`type`**: A constant value of `metadata`, indicating that this section of the payload contains metadata about the webhook.
- **`createdDate`**: The creation date of the webhook event.
- **`eventType`**: The type of event associated with the webhook, which can be `BUILD_CREATED`, `BUILD_STARTED`, `BUILD_COMPLETED`, or `UNRECOGNIZED`.

##### App

- **`id`**: A string that uniquely identifies the app associated with the webhook, such as `12345678-abcd-1234-5678-a12345bc4567`.
- **`type`**: A constant value of `apps`, indicating that this section of the payload contains app information for the event.

##### Ciworkflow

- **`id`**: A string that uniquely identifies the workflow associated with the webhook, such as `12345678-abcd-1234-5678-a12345bc4567`.
- **`type`**: A constant value of `ciWorkflows`, indicating that this data structure represents a workflow.
- **`name`**: The name of the workflow associated with the webhook.
- **`description`**: The description of the workflow in the workflow editor.
- **`lastModifiedDate`**: The date of the workflow’s most recent modification.
- **`isEnabled`**: A Boolean value that indicates whether the workflow is currently in an enabled state.
- **`isLockedForEditing`**: A Boolean value that indicates whether the workflow is locked for editing, preventing any modifications.

##### Ciproduct

- **`id`**: A string that uniquely identifies the product associated with the webhook, such as `12345678-abcd-1234-5678-a12345bc4567`.
- **`type`**: A constant value of `ciProducts`, indicating that this data structure represents a product.
- **`name`**: The name of the product associated with the webhook.
- **`createdDate`**: The creation date of the product.
- **`productType`**: The type of product associated with the webhook, such as `APP` or `FRAMEWORK`.

##### Cibuilds

- **`id`**: A string that uniquely identifies the build associated with the webhook, such as `12345678-abcd-1234-5678-a12345bc4567`.
- **`type`**: A constant value of `ciBuildRuns`, indicating that this data structure represents a build.
- **`number`**: The number of the current build, such as `42`.
- **`createdDate`**: The creation date or scheduled date of the build.
- **`startedDate`**: The start date of the build execution.
- **`finishedDate`**: The finish date of the build execution.

**sourceCommit** - The `git` commit and SCM details for the build.

- **`commitSha`**: The unique SHA-1 hash of the source commit.
- **`author`**: The display name of the source commit author.
- **`committer`**: The display name of the person who commits the change.
- **`htmlUrl`**: The URL that links to the change on the SCM provider’s website.

**destinationCommit** - Optional commit details of the target commit associated with the build.

- **`commitSha`**: The unique SHA-1 hash of the destination commit.
- **`author`**: The display name of the destination commit author.
- **`committer`**: The display name of the person who commits the change.
- **`htmlUrl`**: The URL that links to the change on the SCM provider’s website.
- **`isPullRequestBuild`**: A Boolean value that indicates whether a pull request triggered the build.
- **`executionProgress`**: The current progress of the build, which can be `PENDING`, `RUNNING`, or `COMPLETE`.
- **`completionStatus`**: The completion status of the build, which can be `SUCCEEDED`, `FAILED`, `ERRORED`, `CANCELED`, or `SKIPPED`.

##### Cibuildactions

Information and metadata for each build action that runs as part of the build.

- **`id`**: A string that uniquely identifies the build action list.
- **`type`**: A constant value of `ciBuildActions`, indicating that this data structure represents a build action.
- **`name`**: The name of the build action.
- **`actionType`**: The type of build action, which can be `BUILD`, `ANALYZE`, `TEST`, or `ARCHIVE`.
- **`startedDate`**: The start date of the build action execution.
- **`finishedDate`**: The finish date of the build action execution.

**issueCounts**

- **`analyzerWarnings`**: An integer value representing the number of analyzer warnings associated with the build.
- **`errors`**: An integer value representing the number of errors associated with the build.
- **`testFailures`**: An integer value representing the number of test failures associated with the build.
- **`warnings`**: An integer value representing the number of warnings associated with the build.
- **`relationships`**: The build relationship details, including the platform type. Possible platform types are `IOS`, `MAC_OS`, or `TV_OS`.

**builds**

- **`id`**: The unique identifier of the build associated with the build action.
- **`type`**: A constant value of `builds`, indicating that this data structure represents a build.
- **`platform`**: The platform type associated with the build, such as `IOS`, `MAC_OS`, or `TV_OS`.

##### Scmprovider

- **`type`**: A constant value of `scmProviders`, indicating that this data structure represents an SCM provider.

**scmProviderType**

- **`scmProviderType`**: A string value representing the type of the SCM provider, such as `GitHub` or `Bitbucket`.
- **`displayName`**: A string representation of the `ScmProviderType`, such as `GitHub` or `Bitbucket`.
- **`isOnPremise`**: A Boolean value that indicates whether the SCM provider is self-hosted.
- **`endpoint`**: The URL of the repository on the SCM provider’s website.

##### Scmrepository

- **`id`**: A string that uniquely identifies the SCM repository.
- **`type`**: A constant value of `scmRepositories`, indicating that this data structure represents an SCM repository.
- **`httpCloneUrl`**: The HTTP clone URL of the repository.
- **`sshCloneUrl`**: The optional SSH clone URL of the repository.
- **`ownerName`**: The name of the person or organization that owns the repository.
- **`repositoryName`**: The name of the repository associated with the build.

##### Scmpullrequest

- **`id`**: A string that uniquely identifies the pull request.
- **`type`**: A constant value of `scmPullRequests`, indicating that this data structure represents an SCM pull request.
- **`title`**: The title of the pull request.
- **`number`**: The number of the current pull request, such as `123`.
- **`htmlUrl`**: The HTML URL of the pull request, such as `https://example.com/example/example-app/pull/123`.
- **`sourceRepositoryOwner`**: The owner of the source repository.
- **`sourceRepositoryName`**: The name of the source repository.
- **`sourceBranchName`**: The name of the branch in the source repository where someone created the pull request, such as `annejohnson/new-features`.
- **`destinationRepositoryOwner`**: The owner of the destination repository.
- **`destinationRepositoryName`**: The name of the destination repository.
- **`destinationBranchName`**: The name of the branch in the destination repository to merge the changes into.
- **`isClosed`**: A Boolean value that indicates whether the pull request is closed.
- **`isCrossRepository`**: A Boolean value that indicates whether the pull request is between repositories that different users or organizations own.

##### Scmgitreference

- **`id`**: A string that uniquely identifies the Git reference.
- **`type`**: A constant value of `scmGitReferences`, indicating that this data structure represents an SCM Git reference.
- **`name`**: The human-readable name of the Git reference.
- **`canonicalName`**: The fully qualified name of the Git reference, such as `refs/heads/bug-fix`. This uniquely identifies a specific branch, tag, or other reference.
- **`isDeleted`**: A Boolean value that indicates whether the Git reference is deleted.
- **`kind`**: The type of Git reference, such as `branch` or `tag`.

## See Also

- [Configuring webhooks in Xcode Cloud](configuring-webhooks-in-xcode-cloud.md)
  Send build events to external services and tools using webhooks.
- [Connecting Xcode Cloud to Slack](connecting-xcode-cloud-to-slack.md)
  Connect Xcode Cloud to Slack to keep your team informed about the latest Xcode Cloud builds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/webhook-payload)*