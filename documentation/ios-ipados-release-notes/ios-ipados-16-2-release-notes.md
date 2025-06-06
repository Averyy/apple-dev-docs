# iOS & iPadOS 16.2 Release Notes

**Framework**: iOS & iPadOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The iOS & iPadOS 16.2 SDK provides support to develop apps for iPhone and iPad running iOS & iPadOS 16.2. The SDK comes bundled with Xcode 14.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 14.2, see [`Xcode 14.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-14_2-release-notes).

##### Swiftui

###### New Features

- Disable animations of `NavigationStack` push and pop by wrapping path mutation in `withTransaction(transaction) { … }` where `transaction` has `disablesAnimations` set to `true`. (88993253)

###### Deprecations

- In order to improve compiler type-checking performance, we’ve deprecated some `Table` initializers. They’re replaced with initializers which require an additional parameter that explicitly specifies the type they generate their contents from. This improves type-check performance by avoiding the need to infer a shared type from the bodies of separate closure parameters. For now, these initializers are deprecated. In a future release, those deprecation warnings will become errors. The new initializers add the parameter `of:`. The new initializers add the parameter `of:`. The following shows a Table before, and after adoption of the new API: ```swift
// before (will now produce an error):
Table {
  TableColumn("Name", value: \.name)
  TableColumn("Email", value: \.email)
} rows: {
  ForEach(people) { person in
      TableRow(person)
  }
}

// after:
Table(of: Person.self) {
  TableColumn("Name", value: \.name)
  TableColumn("Email", value: \.email)
} rows: {
  ForEach(people) { person in
      TableRow(person)
  }
}
``` (101009480)

## See Also

- [iOS & iPadOS 16.6 Release Notes](ios-ipados-16_6-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.5 Release Notes](ios-ipados-16_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.4 Release Notes](ios-ipados-16_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS & iPadOS 16.3 Release Notes](ios-ipados-16_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS 16.1 Release Notes](ios-16_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iOS 16 Release Notes](ios-16-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [iPadOS 16 Release Notes](ipados-16-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-16_2-release-notes)*