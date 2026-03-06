# Personalize

**Framework**: Wallet Passes  
**Kind**: dictionary

An object that contains the personalization information for a rewards pass.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- watchOS 3.0+

## Declaration

```swift
object Personalize
```

## Properties

- `description` (string) *(required)*: A brief description of the program for a pass that appears on the signup sheet, under the personalization logo.
- `requiredPersonalizationFields` ([string]) *(required)*: An array that identifies the signup data required from the user the system shows on the generated signup form.
- `termsAndConditions` (string): A description of the program’s terms and conditions. This string can contain HTML link tags to external content. If present, this information appears after the user enters their personal information and taps the Next button. The user then has the option to agree to the terms, or to cancel the sign-up process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/personalize)*