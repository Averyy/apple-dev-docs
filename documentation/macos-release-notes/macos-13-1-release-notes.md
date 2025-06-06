# macOS Ventura 13.1 Release Notes

**Framework**: macOS Release Notes

Update your apps to use new features, and test your apps against API changes.

#### Overview

The macOS 13.1 SDK provides support to develop apps for Mac computers running macOS Ventura 13.1. The SDK comes bundled with Xcode 14.2, available from the Mac App Store. For information on the compatibility requirements for Xcode 14.2, see [`Xcode 14.2 Release Notes`](https://developer.apple.com/documentation/Xcode-Release-Notes/xcode-14_2-release-notes).

##### Endpoint Security

###### Resolved Issues

- Fixed: Third-party security products using the Endpoint Security API might lose Full Disk Access authorization and stop functioning, even though the product remains visible in System Settings. This issue doesn’t affect authorization granted via MDM. (100857507)

##### Swiftui

###### Deprecations

- In order to improve compiler type-checking performance, we’ve deprecated, and will eventually remove some existing Table initializers. They have been replaced with initializers which require an additional parameter that explicitly specifies the type they generate their contents from. This improves type-check performance by avoiding the need to infer a shared type from the bodies of separate closure parameters. For now, these problematic intiializers have been deprecated. The new initializers add the parameter `of:`. The following shows a Table before, and after adoption of the new API: ```swift
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

##### Swiftui Navigation

###### Resolved Issues

- Fixed: NavigationStack on macOS supports animated transitions. Either pass the `path` argument to `NavigationStack` with an animated binding (`$path.binding`), or mutate the path within a `withAnimation` body. The `transition` modifier now has an effect on pushed destinations. For example:

```None
private struct AnimatedStacks: View {
    @State private var path: [Int] = []
    private var colors: [Color] = [.red, .green, .blue, .pink]

    var body: some View {
        NavigationStack(path: $path.animation()) {
            VStack {
                List(0..<3) { int in
                    NavigationLink(value: int) {
                        Text("Animated Option")
                    }
                }
                Button("Option 2") {
                    withAnimation {
                        path.append(3)
                    }
                }
            }
            .navigationDestination(for: Int.self) { int in
                if int == 2 {
                    colors[int].transition(.opacity)
                } else {
                    colors[int]
                }
            }
        }
        .toolbar {
            Spacer()
        }
    }
}
```

(95714581)

## See Also

- [macOS Ventura 13.5 Release Notes](macos-13_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.4 Release Notes](macos-13_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.3 Release Notes](macos-13_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13.2 Release Notes](macos-13_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Ventura 13 Release Notes](macos-13-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-13_1-release-notes)*