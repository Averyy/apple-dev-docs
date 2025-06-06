# Adding a Web Service to Update Passes

**Framework**: Walletpasses

Implement a web server to register, update, and unregister a pass on a device.

#### Overview

Keep your users’ pass updated with the latest information, such as the time of a flight or the location of the next geocached object in a game.

![A diagram of the client and server flow for a user to update a pass. The server creates a pass which the user installs. Some time later the pass is updated, the server and client go through the update flow, and at some later time the user views the pass.](https://docs-assets.developer.apple.com/published/6a8e13984b4c1a7bdf413aed9e357a55/media-3737830%402x.png)

Create an updatable pass by adding the `webServiceURL` and `authenticationToken` keys to [`Pass`](pass.md). The system calls your server endpoints using the base URL you provide. Updating a pass is a cooperative effort between the user’s device, Apple servers, and your server. The high-level steps are:

1. The user installs a pass that supports updates on their device.
2. The user’s device registers the pass with your server and provides a device identifier and a push token.
3. Pass information changes and your server sends a push notification.
4. The user’s device receives the notification and queries your server for updated passes.
5. The user’s device requests each pass that has changed.

##### Server Configuration

Authenticate each call to your server using a shared secret before responding using one of two shared secrets. Use the value of `authenticationToken` for the pass to authenticate the calls that register and unregister a pass, and to send an updated pass. The other shared secret is the , a value that’s sent by the device when the device registers a pass. Use this secret to authenticate the call for the serial numbers of updated passes.

> **Note**:  Your web service must use an HTTPS connection for production, but you can use an HTTP connection during testing.

###### Store Information

Updating passes requires storing information for the registered passes and for their associated devices. One way you can store these details is to use a traditional relational database with two entities – devices and passes – and one relationship, registrations. The three tables are:

##### Register and Unregister a Pass

Add the relationship when a device registers an updatable pass.

![An illustration that shows the call to register a pass. The client sends the server a pass type ID, serial number, authentication token, device library ID, and a push token.](https://docs-assets.developer.apple.com/published/844b5602687e1b03836d55f776daf84e/media-3737836%402x.png)

Complete these tasks to register a pass:

- Create a new entry for the pass if one doesn’t exist.
- Create a new entry for the device if one doesn’t exist.
- Store the mapping between the pass and the device library identifier in the registrations table.

Remove the relationship when a device unregisters an updateable pass.

![An illustration that shows the call to unregister a pass. The client sends the server a pass type ID, serial number, authentication token, and device library ID.](https://docs-assets.developer.apple.com/published/8229d2e7d19a0a591cf90929469c6c89/media-3737831%402x.png)

Complete these tasks to unregister a pass:

- Delete the mapping between the pass and the device library identifier from the registrations table.
- Delete the device entry from the device table if the registration table has no more entries for that device.

##### Update a Pass

You can update any type of pass and any information in the pass, except for the authentication token and the serial number. An updated pass is a new pass with the same pass type identifier and serial number. For more information on creating a pass, see [`Creating the Source for a Pass`](creating-the-source-for-a-pass.md) and [`Building a Pass`](building-a-pass.md).

Updating the pass involves several steps for both your server and the client device that contains the pass:

- Your server sends a push notification to the device.
- The device requests the serial numbers for updated passes.
- Your server sends the serial numbers for the updated passes.
- The device requests a specific pass.
- Your server sends the updated pass.

###### Send a Push Notification

![An illustration that shows the flow of sending an update notification to a client device. The server sends an Apple Push Notification for a pass type ID using the push token for the device.](https://docs-assets.developer.apple.com/published/01e4d374e824d44b0fef1464bae944df/media-3737835%402x.png)

Send a push notification to a registered device to indicate that there’s an updated pass. Do this using the following steps:

- Find the registered devices for the updated pass.
- Create and send a push notification for each registered device. The notification uses the same certificate and private key that the creator of the pass used to sign the original, the push token registered by the device, and an empty JSON dictionary for the payload.

Delete a device if the Apple Push Notification service (APNs) returns an error that the push token is invalid.

For more information on sending push notifications, see [`Sending notification requests to APNs`](https://developer.apple.com/documentation/UserNotifications/sending-notification-requests-to-apns).

> **Note**:  A push notification for a pass update works only in the production environment.

###### Return the Updated Passes

A device that receives the push notification requests a list of serial numbers for updated passes, such as a tickets to an event. Your server sends the serial numbers for updated passes.

![An illustration that shows the flow of updating a pass. The client sends the pass type ID, device library ID, and an update tag to request the updated passes. The server then sends the updated serial numbers with an update tag. The client then requests an updated pass sending a pass type ID, serial number and authentication. Finally the server sends the pass data.](https://docs-assets.developer.apple.com/published/62440eba4f5b58a5b78a014a1a00d490/media-3737834%402x.png)

Keep track of the update time of a pass to limit the number of serial numbers your server sends when a device requests the updated passes. Set the `lastUpdated` key of [`SerialNumbers`](serialnumbers.md) to the last update time. The device saves the value and uses it to set the `previousLastUpdated` command line argument of [`Get the List of Updatable Passes`](get-the-list-of-updatable-passes.md).

To send the list of serial numbers:

1. Find the list of passes registered for the device using the registrations table.
2. Select the passes that have been updated since your web service provided the `updated` tag, or all passes when there’s no tag. If there are multiple updates to a pass, select the one with the most recent update.
3. Create the [`SerialNumbers`](serialnumbers.md) JSON response dictionary and send it with the response. For example:

```other
{
    "serialNumbers" : ["001", "020", "3019"],
    "lastUpdated" : "1351981923"
}
```

The device then sends a request to your server for each updated pass.

## See Also

- [Register a Pass for Update Notifications](register-a-pass-for-update-notifications.md)
  Set up change notifications for a pass on a device.
- [Get the List of Updatable Passes](get-the-list-of-updatable-passes.md)
  Send the serial numbers for updated passes to a device.
- [Send an Updated Pass](send-an-updated-pass.md)
  Create and sign an updated pass, and send it to the device.
- [Unregister a Pass for Update Notifications](unregister-a-pass-for-update-notifications.md)
  Stop sending update notifications for a pass on a device.
- [Log a Message](log-a-message.md)
  Record a message on your server.
- [object PushToken](pushtoken.md)
  An object that contains the push notification token for a registered pass on a device.
- [object SerialNumbers](serialnumbers.md)
  An object that contains serial numbers for the updatable passes on a device.
- [object LogEntries](logentries.md)
  An object that contains an array of messages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WalletPasses/adding-a-web-service-to-update-passes)*