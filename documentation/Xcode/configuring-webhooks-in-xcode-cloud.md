# Configuring webhooks in Xcode Cloud

**Framework**: Xcode

Configure webhooks that connect Xcode Cloud to other services and tools.

#### Overview

You might use custom services and tools in your development process and for project management purposes and need to connect them to Xcode Cloud. For example, you might want to show build information from Xcode Cloud on your team’s dashboard, automate the merge process for pull requests (PRs), automatically open or close issues in your issue tracking tool, and so on.

To connect Xcode Cloud with a custom tool or service, you need to configure an HTTPS endpoint that can receive HTTP requests from Xcode Cloud, referred to as a . By configuring a webhook, you enable Xcode Cloud to send a rich JSON payload to another service or tool at certain moments during the build process. The service or tool can then parse the JSON payload and use the received information to provide its functionality.

> **Note**: You can configure up to five webhooks per Xcode Cloud product.

You can configure up to five webhooks per Xcode Cloud product.

Xcode Cloud sends an HTTP request to each webhook’s configured HTTPS endpoint every time it creates, starts, and finishes a build.

![An illustration that shows the different moments when Xcode Cloud sends a JSON payload to the configured endpoint: when it creates, starts, and finishes a new build.](https://docs-assets.developer.apple.com/published/0a9e7a570ecb8754fe39342feeff1aa9/Configuring-Webhooks-in-Xcode-Cloud-1%402x.png)

For more information about creating webhooks in Xcode Cloud, see [`Customize your advanced Xcode Cloud workflows`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10269).

##### Create an Xcode Cloud Webhook

To create a webhook in Xcode Cloud:

1. In [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com), choose an app and select the Xcode Cloud tab.
2. In the sidebar, choose Settings > Webhooks.
3. Click the Add button (+) to add a new webhook.
4. Choose a unique, easily recognizable name for the webhook, like “Team Dashboard” or “Issue Tracker”.
5. Enter the URL of an app or service that’s capable of receiving and handling HTTPS requests.

When your service or tool receives a request from Xcode Cloud, respond with an HTTP status code that indicates success. If you return a retry-able server error or Xcode Cloud doesn’t receive a response within 30 seconds, it resends the webhook request until it receives a successful response.

> **Note**: You need to configure a project or workspace to use Xcode Cloud before you can create a webhook.

You need to configure a project or workspace to use Xcode Cloud before you can create a webhook.

##### Debug a Webhook

When you create a new webhook, plan to spend some time making sure your service or tool can parse the JSON payload that Xcode Cloud sends. To help you debug an integration problem, Xcode Cloud records a delivery report for each webhook request it sends. It includes detailed request and response metadata.

To access a webhook’s delivery report:

1. In [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com) choose your app and select the Xcode Cloud tab.
2. In the sidebar, choose Settings > Webhooks.
3. Choose a webhook and review its delivery reports.

##### Review the Payload

With each webhook request, Xcode Cloud includes detailed information about the app you configured in App Store Connect, the workflow that started the build, the build itself, your Git repository, and more. Use this information to provide functionality in your custom tool or service. For example, use the payload information to display Xcode Cloud build information on your team’s dashboard.

For more information on webhook payloads, see [`Xcode Cloud webhook payload reference`](webhook-payload.md).

The following code snippet shows the payload Xcode Cloud sends with a request:

```json
{
    "webhook": {
        "id": "12345678-abcd-1234-5678-a12345bc4567",
        "name": "Issue Tracker",
        "url": "https://issues.example.com/webhooks"
    },
    "metadata" : {
        "type" : "metadata",
        "attributes" : {
            "createdDate" : "2021-06-07T10:00:00.000000-07:00",
            "eventType" : "BUILD_COMPLETED"
        }
    },
    "app": {
        "id": "12345678-abcd-1234-5678-a12345bc4567",
        "type": "apps"
    },
    "ciWorkflow": {
        "id": "12345678-abcd-1234-5678-a12345bc4567",
        "type": "ciWorkflows",
        "attributes": {
            "name": "Pull Requests",
            "description": "Starts Builds from Pull Requests.",
            "isEnabled": true,
            "isLockedForEditing": false
        }
    },
    "ciProduct": {
        "id": "12345678-abcd-1234-5678-a12345bc4567",
        "type": "ciProducts",
        "attributes": {
            "name": "Example App",
            "createdDate": "2021-06-07T10:00:00.000000-07:00",
            "productType": "APP"
        }
    },
    "ciBuildRun": {
        "id": "12345678-abcd-1234-5678-a12345bc4567",
        "type": "ciBuildRuns",
        "attributes": {
            "number": 12,
            "createdDate": "2021-06-07T10:00:00.000000-07:00",
            "sourceCommit": {
                "commitSha": "0123456789abcdefghij01234567890abcdefghi",
                "author": {
                    "displayName": "Anne Johnson"
                },
                "committer": {
                    "displayName": "Anne Johnson"
                },
                "htmlUrl": "https://example.com/commit/abcdef1234567890"
            },
            "destinationCommit": {
                "commitSha": "abcdefghij01234567890abcdefghi0123456789",
                "author": {
                    "displayName": "Juan Chavez"
                },
                "committer": {
                    "displayName": "Juan Chavez"
                },
                "htmlUrl": "https://example.com/commit/abcdef1234567890"
            },
            "isPullRequestBuild": true,
            "executionProgress": "COMPLETE",
            "completionStatus": "SUCCEEDED"
        }
    },
    "ciBuildActions": [{
        "id": "12345678-abcd-1234-5678-a12345bc4567",
        "type": "ciBuildActions",
        "attributes": {
            "name": "analyze",
            "actionType": "ANALYZE",
            "issueCounts": {
                "analyzerWarnings": 10,
                "errors": 0,
                "testFailures": 0,
                "warnings": 0
            },
            "executionProgress": "COMPLETE",
            "completionStatus": "SUCCEEDED",
            "isRequiredToPass": false
        },
        "relationships": {}
    }, {
        "id": "12345678-abcd-1234-5678-a12345bc4567",
        "type": "ciBuildActions",
        "attributes": {
            "name": "build",
            "actionType": "ARCHIVE",
            "issueCounts": {
                "analyzerWarnings": 0,
                "errors": 0,
                "testFailures": 0,
                "warnings": 3
            },
            "executionProgress": "COMPLETE",
            "completionStatus": "SUCCEEDED",
            "isRequiredToPass": true
        },
        "relationships": {
            "builds": {
                "id": "12345678-abcd-1234-5678-a12345bc4567",
                "type": "builds",
                "attributes": {
                    "platform": "IOS"
                }
            }
        }
    }],
    "scmProvider": {
        "type": "scmProviders",
        "attributes": {
            "scmProviderType": {
                "scmProviderType": "GITHUB_CLOUD",
                "displayName": "GitHub",
                "isOnPremise": false
            },
            "endpoint": "https://github.com/example/example.git"
        }
    },
    "scmRepository": {
        "id": "12345678-abcd-1234-5678-a12345bc4567",
        "type": "scmRepositories",
        "attributes": {
            "httpCloneUrl": "https://github.com/example/test.git",
            "sshCloneUrl": "ssh://git@github.com/example/test.git",
            "ownerName": "example",
            "repositoryName": "example app"
        }
    },
    "scmPullRequest": {
        "id": "12345678-abcd-1234-5678-a12345bc4567",
        "type": "scmPullRequests",
        "attributes": {
            "title": "Add accessibility labels.",
            "number": 123,
            "htmlUrl": "https://example.com/example/example-app/pull/123",
            "sourceRepositoryOwner": "example",
            "sourceRepositoryName": "example source repository name",
            "sourceBranchName": "annejohnson/new-features",
            "destinationRepositoryOwner": "example",
            "destinationRepositoryName": "example destination repository name",
            "destinationBranchName": "main",
            "isClosed": false,
            "isCrossRepository": false
        }
    },
    "scmGitReference": {
        "id": "12345678-abcd-1234-5678-a12345bc4567",
        "type": "scmGitReferences",
        "attributes": {
            "name": "annejohnson/new-feature",
            "canonicalName": "refs/heads/annejohnson/new-feature",
            "isDeleted": false,
            "kind": "BRANCH"
        }
    }
}
```

## See Also

- [Xcode Cloud webhook payload reference](webhook-payload.md)
  Review details of the webhook payload that Xcode Cloud sends, including the product, workflow, build, actions, results, and SCM metadata associated with it.
- [Connecting Xcode Cloud to Slack](connecting-xcode-cloud-to-slack.md)
  Connect Xcode Cloud to Slack to keep your team informed about the latest Xcode Cloud builds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/configuring-webhooks-in-xcode-cloud)*