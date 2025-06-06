# Implementing communication notifications

**Framework**: Usernotifications

Configure and display your app’s communication notifications by using intents.

#### Overview

Communication notifications provide a rich experience for direct communications. These notifications have a distinct user experience that features prominent avatars and group names. Communication notifications are unique in their ability to break through the scheduled notification summary by default, and can also break through a Focus.

Enable the Communication Notifications capability in your app and include the activity types that your app supports in its `NSUserActivityTypes` array. Your app initializes relevant participants of the communication, configures an intent object that describes the communication taking place, and then donates the interaction. Siri uses these donations to refine suggestions given to the user. After your app donates the interaction, your app updates the incoming notification’s content and displays a communication notification. To learn more about SiriKit interaction donations, see [`Donating Shortcuts`](https://developer.apple.com/documentation/SiriKit/donating-shortcuts).

##### Enable Communication Notifications

Enable the Communication Notifications capability in your app target before you implement communication notifications. To learn more about enabling capabilities, see [`Adding capabilities to your app`](https://developer.apple.com/documentation/Xcode/adding-capabilities-to-your-app). Add the class name of each intent that your app supports to the `NSUserActivityTypes` array in your `Info.plist`. To support [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) donations, for example, ensure the `NSUserActivityTypes` array includes the string `INSendMessageIntent`.

Once you enable the Communications Notifications capability, begin updating the content of notifications that your app receives so it can display communication notifications. Implement this functionality wherever your app can receive notifications, including your app’s Notification Service Extension (NSE), which you use to modify the content of incoming notifications when your app is in the background. For more information about handling notifications in the background, refer to [`Modifying content in newly delivered notifications`](modifying-content-in-newly-delivered-notifications.md).

##### Identify the Participants

You must include relevant participants in communication notifications to ensure correct display and breakthrough behavior. Create an [`INPerson`](https://developer.apple.com/documentation/Intents/INPerson) object for each relevant participant of a communication when your app receives a communication notification. The current user is always a recipient of an incoming communication notification. Don’t include the current user as a participant of the communication for your app’s intent donations.

If a person in your app matches a contact in address book, provide the contact identifier when initializing the [`INPerson`](https://developer.apple.com/documentation/Intents/INPerson) object. If your app has access to a person’s email address or phone number, provide a person handle type of [`INPersonHandleType.emailAddress`](https://developer.apple.com/documentation/Intents/INPersonHandleType/emailAddress) or [`INPersonHandleType.phoneNumber`](https://developer.apple.com/documentation/Intents/INPersonHandleType/phoneNumber) respectively, and also specify the person’s suggestion type as [`INPersonSuggestionType.none`](https://developer.apple.com/documentation/Intents/INPersonSuggestionType/none). Providing both of these types ensures an exact match for the corresponding email address or phone number in the user’s contacts.

If the information necessary to ensure an exact match isn’t available, create an [`INPersonHandle`](https://developer.apple.com/documentation/Intents/INPersonHandle) specific to your app. Set the person’s [`INPersonSuggestionType`](https://developer.apple.com/documentation/Intents/INPersonSuggestionType) to whichever type it most closely resembles, which provides a contact suggestion to the user if a matching contact isn’t found.

##### Configure a Message Intent

When the user receives a message, you create an [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent). An [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) has a single sender and one or more recipients. For incoming communication notification donations, the system includes the current user as a recipient in addition to those your app provides in the `recipients` array. Provide a unique `conversationIdentifier` that represents the conversation. Use the same identifier for each message that the user receives in the same conversation. This is especially important for group conversations where the group name and membership can change for each message.

The example below represents a direct message. There are no recipients other than the current user in this case. The `image` of the sender becomes the avatar for the notification.

```swift
// Initialize only the sender for a one-to-one message intent.
let handle = INPersonHandle(value: "unique-user-id-1", type: .unknown)
let avatar = INImage(named: "profilepicture.png")
let sender = INPerson(personHandle: handle,
                      nameComponents: nil,
                      displayName: "Example",
                      image: avatar,
                      contactIdentifier: nil,
                      customIdentifier: nil)

// Because this communication is incoming, you can infer that the current user is
// a recipient. Don't include the current user when initializing the intent.
let intent = INSendMessageIntent(recipients: nil,
                                 outgoingMessageType: .outgoingMessageText,
                                 content: "Message content",
                                 speakableGroupName: nil,
                                 conversationIdentifier: "unique-conversation-id-1",
                                 serviceName: nil,
                                 sender: sender,
                                 attachments: nil)
```

For group message intents, provide an array that contains the other participants of the message for the `recipients` parameter. For example, in a group of three participants that includes the current user, the `sender` of the message and the current user are already represented. The `recipients` array contains one object — the other recipient. Group conversations can also provide a [`speakableGroupName`](https://developer.apple.com/documentation/Intents/INSendMessageIntent/speakableGroupName) if the conversation has a name. The notification shows a summary of the recipients if your app doesn’t provide one. Call [`setImage:forParameterNamed:`](https://developer.apple.com/documentation/intents/inintent/2976224-setimage) on the intent using the [`speakableGroupName`](https://developer.apple.com/documentation/Intents/INSendMessageIntent/speakableGroupName) parameter to provide an avatar for a group message. Set the avatar image prior to donating the interaction.

##### Configure a Call Intent

When the user receives an incoming call, you create an [`INStartCallIntent`](https://developer.apple.com/documentation/Intents/INStartCallIntent). An [`INStartCallIntent`](https://developer.apple.com/documentation/Intents/INStartCallIntent) has an array of one or more contacts that are participants of the call. For incoming communication notification donations, the system includes the current user as a recipient in addition to those added to the `contacts` array. Provide the most accurate additional information available about the call, including a callback record to use in the event of a missed call. The example below represents a call between `caller` and the current user. The caller’s image becomes the avatar for the notification.

```swift
// Initialize only the caller for a one-to-one call intent.
let handle = INPersonHandle(value: "unique-user-id-1", type: .unknown)
let avatar = INImage(named: "profilepicture.png")
let caller = INPerson(personHandle: handle,
                      nameComponents: nil,
                      displayName: "Example",
                      image: avatar,
                      contactIdentifier: nil,
                      customIdentifier: nil)

// Include the other participants of the call in the contacts array.
// Because this communication is incoming, you can infer that the current user is
// a participant of the call. Don't include the user in the contacts array.
let intent = INStartCallIntent(callRecordFilter: nil,
                               callRecordToCallBack: callRecordToCallBack,
                               audioRoute: .bluetoothAudioRoute,
                               destinationType: .normal,
                               contacts: [caller],
                               callCapability: .audioCall)
```

For group call intents, add the other participants to the `contacts` parameter array. In a group of three participants that includes the current user, for example, only include the caller and the third participant in the `contacts` array. Call [`setImage:forParameterNamed:`](https://developer.apple.com/documentation/intents/inintent/2976224-setimage) on the intent using the [`callRecordToCallBack`](https://developer.apple.com/documentation/Intents/INStartCallIntent/callRecordToCallBack) parameter to provide an avatar for a group call. Set the avatar image prior to donating the interaction.

##### Donate an Interaction and Update the Notification

After you configure a communication intent, donate an interaction for the intent. Initialize an [`INInteraction`](https://developer.apple.com/documentation/Intents/INInteraction) object from the previously configured message or call intent. Set the interaction’s direction to [`INInteractionDirection.incoming`](https://developer.apple.com/documentation/Intents/INInteractionDirection/incoming). This indicates the user is the recipient of an interaction — the incoming communication. Call [`donate(completion:)`](https://developer.apple.com/documentation/Intents/INInteraction/donate(completion:)) on the interaction and handle errors that may occur in its completion handler.

If the donation completes successfully, update the content of a received notification to display a communication notification. Call [`updating(from:)`](unnotificationcontent/updating(from:).md) on the received notification content. Use the updated notification content to display a communication notification. In the example below, the handling of this process happens in an NSE. Call the `contentHandler` with the updated notification content to display a communication notification before returning from the [`didReceive(_:withContentHandler:)`](unnotificationserviceextension/didreceive(_:withcontenthandler:).md) method.

```swift
func didReceive(_ request: UNNotificationRequest,
                withContentHandler contentHandler:
                @escaping (UNNotificationContent) -> Void) async {

    // Create an intent as shown in previous code listings.
    // For an incoming message, refer to the first code listing.
    // For an incoming call, refer to the second code listing.
    let intent: INSendMessageIntent = sendMessageIntent()

    // Use the intent to initialize the interaction.
    let interaction = INInteraction(intent: intent, response: nil)

    // Interaction direction is incoming because the user is
    // receiving this message.
    interaction.direction = .incoming

    // Donate the interaction before updating notification content.
    do {
        try await interaction.donate()
    } catch {
        // Handle errors that may occur during donation.
        return
    }
        
    // After donation, update the notification content.
    let content = request.content
    
    do {
        // Update notification content before displaying the
        // communication notification.
        let updatedContent = try content.updating(from: intent)
        
        // Call the content handler with the updated content
        // to display the communication notification.
        contentHandler(updatedContent)
        
    } catch {
        // Handle errors that may occur while updating content.
    }
}
```

##### Donate Outgoing Interactions

Outgoing interactions are important to enable proper breakthrough behavior. An outgoing interaction represents a decision or action that the user initiates. Siri uses outgoing intent donations to refine suggestions to the user in a variety of ways, including Share Sheet recommendations and contact suggestions.

Initializing an outgoing interaction is similar to initializing an incoming interaction. Set the `direction` of an outgoing interaction to [`INInteractionDirection.outgoing`](https://developer.apple.com/documentation/Intents/INInteractionDirection/outgoing) prior to donating. The process to donate an outgoing [`INStartCallIntent`](https://developer.apple.com/documentation/Intents/INStartCallIntent) interaction is identical to the process to donate incoming interactions. When donating an outgoing [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) interaction, however, the current user becomes the sender. Therefore, leave the `sender` parameter of an outgoing [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) `nil`, and provide the recipients of the message, and any other metadata available.

##### Additional Donation Metadata

You can provide optional donation metadata for message intent donations in the form of [`INSendMessageIntentDonationMetadata`](https://developer.apple.com/documentation/Intents/INSendMessageIntentDonationMetadata) objects. This additional metadata changes the behavior of the interaction donation.

You can manually specify the recipient count and initialize a partial list of relevant recipients when the full list of [`INSendMessageIntent`](https://developer.apple.com/documentation/Intents/INSendMessageIntent) recipients is prohibitively large. Supply an [`INSendMessageIntentDonationMetadata`](https://developer.apple.com/documentation/Intents/INSendMessageIntentDonationMetadata) object to the intent and specify the full [`recipientCount`](https://developer.apple.com/documentation/Intents/INSendMessageIntentDonationMetadata/recipientCount). This recipient count overrides the count of the recipients array on the intent. You must either provide the full recipient list to the intent, or instead provide an accurate recipient count on the intent’s donation metadata.

You can also use a donation metadata object when the user receives messages that explicity mention that user, or reply messages to previous conversations. Use a donation metadata object to specify this behavior. Set [`mentionsCurrentUser`](https://developer.apple.com/documentation/Intents/INSendMessageIntentDonationMetadata/mentionsCurrentUser) and [`isReplyToCurrentUser`](https://developer.apple.com/documentation/Intents/INSendMessageIntentDonationMetadata/isReplyToCurrentUser) to enable these behaviors, respectively, on the communication notification.

Someone can choose to notify a user even when the other user has Focus enabled. Your app requires authorization to access the user’s Focus status for this functionality to work.

- Request authorization by calling [`requestAuthorization(completionHandler:)`](https://developer.apple.com/documentation/Intents/INFocusStatusCenter/requestAuthorization(completionHandler:)) on the default [`INFocusStatusCenter`](https://developer.apple.com/documentation/Intents/INFocusStatusCenter) instance.
- Ensure the user has authorized your app before continuing.
- Set [`notifyRecipientAnyway`](https://developer.apple.com/documentation/Intents/INSendMessageIntentDonationMetadata/notifyRecipientAnyway) on the donation metadata object when the notification should break through Focus and interrupt them.

Reserve this functionality for instances where the sender has explicitly chosen to notify the user anyway. Users only expect an interruption like this after they’ve received a communication notification for a message that Focus silenced on their behalf.

## See Also

- [protocol UNNotificationContentProviding](unnotificationcontentproviding.md)
  A protocol the system uses to provide context relevant to user notifications.
- [class UNNotificationActionIcon](unnotificationactionicon.md)
  An icon associated with an action.
- [class UNMutableNotificationContent](unmutablenotificationcontent.md)
  The editable content for a notification.
- [class UNNotificationContent](unnotificationcontent.md)
  The uneditable content of a notification.
- [class UNNotificationAttachment](unnotificationattachment.md)
  A media file associated with a notification.
- [class UNNotificationSound](unnotificationsound.md)
  The sound played upon delivery of a notification.
- [struct UNNotificationSoundName](unnotificationsoundname.md)
  A string providing the name of a sound file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/implementing-communication-notifications)*