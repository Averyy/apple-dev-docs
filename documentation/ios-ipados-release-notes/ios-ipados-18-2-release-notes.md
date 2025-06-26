# iOS & iPadOS 18.2 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 18.2 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 18.2. The SDK comes bundled with Xcode 16.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 16.2, see [`Xcode 16.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-16_2-release-notes).

##### Accessibility

###### Resolved Issues

- Fixed: If you use the Ignore Trackpad setting, it will be reset after updating to iOS 18.2 Beta.   (139611885)

##### Avfoundation

###### Resolved Issues

- Fixed: In Swift, iterating over `AVCaptureSynchronizedDataCollection` with a `for-in` loop causes a crash.  (135132312)

##### Chatgpt Integration

###### Resolved Issues

- Fixed: For devices with MDM profiles, users with anonymous restrictions are unable to sign out.  (135440023)
- Fixed: Requests to generate images with ChatGPT in Writing Tools might fail.  (138791595)

##### Find My

###### Resolved Issues

- Fixed: Play Sound and Precision Finding features of AirTags, AirPods and third-party Find My-enabled accessories might not work.  (138283512)

##### Genmoji

###### Known Issues

- A personalized Genmoji might not generate without selecting a different person first.  (139676076)  In the People selector screen, select a different person, then reselect the original person.

##### Mail

###### Resolved Issues

- Fixed: Recategorizing an email from a domain with a high number of messages might cause unexpected grouping behavior.  (140360935)

##### Messages

###### Resolved Issues

- Fixed: Messages might not appear in the Messages app.  (138152993)

##### Stickers

###### Resolved Issues

- Fixed: Stickers might not appear in the Emoji keyboard or in the sticker sheet. The sticker sheet is accessed through the Stickers item in Messages or in various other places like Freeform and Markup. You’ll either see missing stickers or a message that states you do not have any stickers.  (138790914)

##### Swiftui

###### Resolved Issues

- Fixed: Compiling in the Swift 6 language mode might cause an `@Entry` error due to “static property `defaultValue` is not concurrency-safe because non-‘Sendable’ type”.  (133885814)
- For apps compiled against iOS 18.2/visionOS 2.2 and run against iOS 18.0/visionOS 2.0, the popover modifier does not respect the arrowEdge argument on iOS, iPadOS, or visionOS, regardless of the deployment target of the app. Now, apps compiled against iOS 18.2/visionOS 2.2 and run against iOS 18.1/visionOS 2.1 and later do respect the arrowEdge argument.  (135231043)
- Fixed: Views won’t accept dropped directories if [`UTType.directory`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/directory) or [`UTType.fileURL`](https://developer.apple.comhttps://developer.apple.com/documentation/uniformtypeidentifiers/uttype-swift.struct/fileurl) are not in the list of accepted content types for drop.  (138158126)

##### Uikit

###### Known Issues

- In iOS 18.2 Beta 3, `-[UIApplication defaultStatusForCategory:error:]` and its Swift equivalent `UIApplication.isDefaultApplication(for:)` are not present.  (139669875)  Build and run against iOS 18.2 Beta 2 to test adoption of this new interface.

##### Uiwritingtoolscoordinator

###### Known Issues

- The two optional delegate methods intended for multiple container support are not available in iOS 18.2 Beta.  (136619485)
- When the UIWritingToolsCoordinator state is `Noninteractive`, textual changes might be applied through the UITextInput Paste API, instead of through `-writingToolsCoordinator:replaceRange:inContext:proposedText:reason:animationParameters:completion:`.  (136631598)
- The delegate method `-writingToolsCoordinator:requestsRangeInContextWithIdentifierForPoint:completion:` does not support asynchronous use of the completion block.  (136824869)  For the correct behavior when a user taps on a proofreading suggestion, the completion block for the method must be executed inline.
- UIWritingToolsCoordinator throws an exception if the delegate returns modified text in `-writingToolsCoordinator:replaceRange:inContext:proposedText:reason:animationParameters:completion:`, when `reason` is `Noninteractive`.  (138775662)  Only return modified text when `reason` is `Interactive`.
- The delegate receives more calls to `-writingToolsCoordinator:selectRanges:inContext:completion:` than necessary.  (138868937)
- On Catalyst, if the delegate does not implement `-isEditable` as an `@objC` method, then Writing Tools will not apply changes to the text.  (139031260)
- The UIWritingToolsCoordinator might quit Writing Tools if a user types in the InteractiveResting state or during operation of the previous/next revision buttons in the UI.  (139196667)
- The UIWritingToolsCoordinator might request underline paths from the delegate at a time when they can’t be calculated.  (139532897)  The delegate must be arranged to send `-updateForReflowedTextInContextWithIdentifier:` to the writingToolsCoordinator when underline paths can be calculated.
- Undo/redo grouping behavior is unpredictable when Writing Tools is active.  (139533079)  For proper undo/redo grouping behavior, the delegate must start the grouping when the UIWritingToolsCoordinator’s state changes to InteractiveStreaming and stop when the state changes away from InteractiveStreaming. When the undo/redo stack is popped, the delegate should notify the Writing Tools coordinator, using `-updateRange:withText:reason:forContextWithIdentifier:` and passing the `UndoRedo` reason for each item. When all the items in the group have popped, use the same method to notify the coordinator, passing a 0-length range and a 0-length attributedString along with `Typing` for the reason.

##### Writing Tools

###### Known Issues

- For third-party apps adopting Writing Tools API on iOS, if the first responder is not a UIView, it will not be able to use the complete inline experience.  (139833232)

## See Also

- [iOS & iPadOS 18.6 Beta Release Notes](ios-ipados-18_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.5 Release Notes](ios-ipados-18_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.4 Release Notes](ios-ipados-18_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.3 Release Notes](ios-ipados-18_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18.1 Release Notes](ios-ipados-18_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 18 Release Notes](ios-ipados-18-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-18_2-release-notes)*