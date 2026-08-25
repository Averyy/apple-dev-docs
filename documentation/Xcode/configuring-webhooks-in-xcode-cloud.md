# Configuring webhooks in Xcode Cloud

**Framework**: Xcode

Send build events to external services and tools using webhooks.

#### Overview

To track Xcode Cloud progress using custom services and tools, connect them to Xcode Cloud using webhooks. For example, display build information from Xcode Cloud on your team’s dashboard, automate the merge process for pull requests (PRs), automatically open or close issues in your issue tracking tool, and so on.

To connect Xcode Cloud with a custom tool or service, configure an HTTPS endpoint that can receive HTTP requests from Xcode Cloud, referred to as a *webhook*. By configuring a webhook, you enable Xcode Cloud to send a rich JSON payload to another service or tool at certain moments during the build process. The service or tool can then parse the JSON payload and use the received information to provide its functionality.

Xcode Cloud sends an HTTP request to each webhook’s configured HTTPS endpoint every time it creates, starts, and finishes a build.

![An illustration that shows the different moments when Xcode Cloud sends a JSON payload to the configured endpoint: when it creates, starts, and finishes a new build.](/images/com.apple.Xcode/Configuring-Webhooks-in-Xcode-Cloud-1@2x.png)

For more information about creating webhooks in Xcode Cloud, see [`Customize your advanced Xcode Cloud workflows`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2021/10269).

> **Note**: Configure your project or workspace to use Xcode Cloud before you create webhooks. You can configure up to five webhooks per Xcode Cloud product.

#### Create an Xcode Cloud Webhook

You need to provide the following information when creating a webhook:

- An easily identifiable name for the webhook, such as “Team Dashboard” or “Issue Tracker”
- A URL for an app or service that can receive and handle HTTPS requests

Also, configure your service or tool to respond with an HTTP status code that indicates success when it receives a request from Xcode Cloud. If it returns a retryable server error or Xcode Cloud doesn’t receive a response within 30 seconds, Xcode Cloud resends the webhook request until it receives a successful response.

To create a webhook using Xcode:

1. In the Report navigator, click the Cloud tab.
2. Control-click your product under the Cloud tab and choose Manage Webhooks from the contextual menu.
3. In the Webhooks pane of the sheet that appears, click the Add button in the lower-left corner.
4. In the Add Webhook dialog, enter a name and payload URL for the webhook, and click Add.
5. Click Done.

![A screenshot that shows the Add Webhook dialog with the name and URL text fields, and Add button.](/images/com.apple.Xcode/add-webhook@2x.png)

Alternatively, create a webhook using [`App Store Connect`](https://developer.apple.comhttps://appstoreconnect.apple.com):

1. In App Store Connect, choose an app and select the Xcode Cloud tab.
2. Click Settings in the sidebar and select the Webhooks tab on the right.
3. Click the Add button (+) next to Webhooks.
4. In the sheet, enter a name and payload URL for the webhook, and click Save.

#### View Webhook Delivery History and Metadata

After Xcode Cloud builds your app, you can see webhook delivery history and other details in Xcode. Use the delivery history to confirm that your service or tool parses the JSON payload that Xcode Cloud sends.

To view delivery history in Xcode:

1. In the Report navigator, control-click your product and choose Manage Webhooks.
2. In the Webhooks pane, click the disclosure triangle to the left of the webhook. The events appear below.
3. To see the request and response metadata, select an event.

To access webhook delivery reports in App Store Connect:

1. Choose your app and select the Xcode Cloud tab.
2. Click Settings in the sidebar and select the Webhooks tab on the right.
3. Choose a webhook and review its delivery reports.

#### Review the Payload

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