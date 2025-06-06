# Wallet Passes

**Framework**: Walletpasses  
**Kind**: module

Create, distribute, and update passes for the Wallet app.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- watchOS 2.0+

#### Overview

![An illustration showing two different passes, each on an iPhone. One pass is a boarding pass for a flight and the other is a membership card.](https://docs-assets.developer.apple.com/published/0eb65bc398c66bc2f9810f8704da9863/media-3737533%402x.png)

 are digital representations of information that might previously be on paper or plastic. They let users take action in the physical world, such as boarding a flight, attending an event, or claiming a coat-check item.

To enable a user to install your pass, you need to:

- Create the source for a pass.
- Build a distributable pass from the source.
- Distribute a pass.

For information on creating and building a pass, see [`Creating the Source for a Pass`](creating-the-source-for-a-pass.md) and [`Building a Pass`](building-a-pass.md). For information on distributing a pass, see [`Distributing and updating a pass`](distributing-and-updating-a-pass.md).

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
### Pass Updates
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
### Personalized Passes
- [Return a Personalized Pass](return-a-personalized-pass.md)
  Create and sign a personalized pass, and send it to a device.
- [object PersonalizationDictionary](personalizationdictionary.md)
  An object that contains the information you use to personalize a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/WalletPasses)*