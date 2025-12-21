# Wallet Passes

**Framework**: Wallet Passes  
**Kind**: module

Create, distribute, and update passes for the Wallet app.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- watchOS 2.0+

#### Overview

 are digital representations of information that previously might have been distributed on paper, plastic, or some other physical item. Passes enable people to take action, including board a flight, attend an event, or redeem a coupon. Use the Wallet Passes framework to create dynamic, interactive passes that stay up-to-date and provide people with relevant information.

With this framework you can:

- Create boarding passes, event tickets, store cards, coupons, and generic passes.
- Update the pass contents in real-time.
- Display multiple upcoming events on a single ticket.
- Integrate with system features like Maps, notifications, and Live Activities.
- Support automatic pass updates with flight tracking for boarding passes.

![An illustration showing three different passes. One pass is a boarding pass for a flight, another pass is a event pass for a concert, and the other is a membership card.](https://docs-assets.developer.apple.com/published/9f2c671f1cb0aa608552e73de100fb90/overview-update-wallet-passes%402x.png)

To enable a person to install your pass, you’ll:

- Create the source for a pass.
- Build a distributable pass from the source.
- Distribute a pass.

You can further tailor passes for a personalized experience and make live updates to different kinds of passes through your server.

## Topics

### Essentials
- [Creating the Source for a Pass](creating-the-source-for-a-pass.md)
  Create the directory structure and add source files and images to define a pass.
- [Building a Pass](building-a-pass.md)
  Build a distributable pass.
- [Distributing and updating a pass](distributing-and-updating-a-pass.md)
  Distribute a pass to your users or update an existing pass.
- [object Pass](pass.md)
  An object that represents a pass.
- [object PassFields](passfields.md)
  An object that represents the groups of fields that display information on the front and back of a pass.
### Boarding passes
- [object Pass.BoardingPass](pass/boardingpass-data.dictionary.md)
  An object that represents the groups of fields that display the information for a boarding pass.
- [object SemanticTags](semantictags.md)
  An object that contains machine-readable metadata the system uses to offer a pass and suggest related actions.
- [object SemanticTagType](semantictagtype.md)
  A compilation of data object types for semantic tags.
### Coupon passes
- [object Pass.Coupon](pass/coupon-data.dictionary.md)
  An object that represents the groups of fields that display the information for a coupon.
### Event passes
- [object Pass.EventTicket](pass/eventticket-data.dictionary.md)
  An object that represents the groups of fields that display the information for an event ticket.
- [object SemanticTags](semantictags.md)
  An object that contains machine-readable metadata the system uses to offer a pass and suggest related actions.
- [object SemanticTagType](semantictagtype.md)
  A compilation of data object types for semantic tags.
- [object UpcomingPassInformationEntry](upcomingpassinformationentry.md)
  An object that represents the ordered list of all upcoming pass information entries.
- [object UpcomingPassInformationEntryType](upcomingpassinformationentrytype.md)
  An object that represents a upcoming pass information entry for an specific upcoming event.
### Generic passes
- [object Pass.Generic](pass/generic-data.dictionary.md)
  An object that represents the groups of fields that display the information for a generic pass.
### Store card passes
- [object Pass.StoreCard](pass/storecard-data.dictionary.md)
  An object that represents groups of fields that show the information for a store card.
### Pass updates
- [Adding a Web Service to Update Passes](adding-a-web-service-to-update-passes.md)
  Implement a web server to register, update, and unregister a pass on a device.
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
### Personalized passes
- [Return a Personalized Pass](return-a-personalized-pass.md)
  Create and sign a personalized pass, and send it to a device.
- [object PersonalizationDictionary](personalizationdictionary.md)
  An object that contains the information you use to personalize a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WalletPasses)*