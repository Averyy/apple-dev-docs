# init(identifier:actions:intentIdentifiers:hiddenPreviewsBodyPlaceholder:options:)

**Framework**: User Notifications  
**Kind**: init  
**Role**: Initializer

Creates a category object containing the specified actions, options, and placeholder text used when previews aren’t shown.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
convenience init(identifier: String, actions: [UNNotificationAction], intentIdentifiers: [String], hiddenPreviewsBodyPlaceholder: String, options: UNNotificationCategoryOptions = [])
```

```objc
+ (instancetype) categoryWithIdentifier:(NSString *) identifier actions:(NSArray<UNNotificationAction *> *) actions intentIdentifiers:(NSArray<NSString *> *) intentIdentifiers hiddenPreviewsBodyPlaceholder:(NSString *) hiddenPreviewsBodyPlaceholder options:(UNNotificationCategoryOptions) options;
```

#### Return Value

An initialized category object.

## Parameters

- `identifier`: The unique identifier for the category. Each category that your app uses must have a unique identifier. Don’t specify an empty string.
- `actions`: The actions to display when the system delivers notifications of this type. When minimal space is available, the system displays only the first two actions in the array. You may specify an empty array for this parameter if you don’t want to display custom actions.
- `intentIdentifiers`: The intent identifier strings that you want to associate with notifications of this type. The Intents framework defines constants for each type of intent that you can associate with your notifications.
- `hiddenPreviewsBodyPlaceholder`: A placeholder string to display when the user has disabled notification previews for the app. Include the characters `%u` (the only supported formatting characters) in the string to represent the number of notifications with the same thread identifier. For example, the string “`%u Messages`” becomes “`2 Messages`” when there are two messages.

  To specify different strings for the singular and plural cases, use the [`localizedUserNotificationString(forKey:arguments:)`](../../Foundation/nsstring/localizedusernotificationstring%28forkey,arguments%29.md) method of [`NSString`](../../Foundation/nsstring.md) to specify the value for this parameter. The key passed to that method contains the identifier of an entry in a `.stringsdict` property list of your project. A strings dictionary lets you specify different formatted strings based on the language rules, and is as described in [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i).
- `options`: Additional options for handling notifications of this type. For a list of possible values, see [`UNNotificationCategoryOptions`](../unnotificationcategoryoptions.md).

## See Also

### Essentials
- [convenience init(identifier: String, actions: [UNNotificationAction], intentIdentifiers: [String], options: UNNotificationCategoryOptions)](./init%28identifier,actions,intentidentifiers,options%29.md)
  Creates a category object containing the specified actions and options.
- [convenience init(identifier: String, actions: [UNNotificationAction], intentIdentifiers: [String], hiddenPreviewsBodyPlaceholder: String?, categorySummaryFormat: String?, options: UNNotificationCategoryOptions)](./init%28identifier,actions,intentidentifiers,hiddenpreviewsbodyplaceholder,categorysummaryformat,options%29.md)
  Creates a category object containing the specified actions, options, placeholder text used when previews aren’t shown, and summary format string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/usernotifications/unnotificationcategory/init(identifier:actions:intentidentifiers:hiddenpreviewsbodyplaceholder:options:))*