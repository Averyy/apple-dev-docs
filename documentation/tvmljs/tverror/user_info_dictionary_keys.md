# User Info Dictionary Keys

**Framework**: TVMLKit JS  
**Role**: API Collection

Keys that exist in the user info dictionary.

## Topics

### Constants
- [NSLocalizedDesciptionKey](./user_info_dictionary_keys/api-1807734-nslocalizeddesciptionkey.md)
  The corresponding value is a localized string representation of the error.
- [NSFilePathErrorKey](./user_info_dictionary_keys/api-1807742-nsfilepatherrorkey.md)
  The corresponding value is a `String` object that contains the file path of the error.
- [NSStringEncodingErrorKey](./user_info_dictionary_keys/api-1807747-nsstringencodingerrorkey.md)
  The corresponding value is a `Number` object containing the `NSStringEncoding` value.
- [NSUnderlyingErrorKey](./user_info_dictionary_keys/api-1807752-nsunderlyingerrorkey.md)
  The corresponding value is an error that was encountered in an underlying implementation and caused the error that the receiver represents to occur.
- [NSURLErrorKey](./user_info_dictionary_keys/api-1807757-nsurlerrorkey.md)
  The corresponding value is an NSURL object.
- [NSLocalizedFailureReasonErrorKey](./user_info_dictionary_keys/api-1807762-nslocalizedfailurereasonerrorkey.md)
  The corresponding value is a localized string representation containing the reason for the failure that, if present, will be returned by [`localizedFailureReason`](../../Foundation/nserror/localizedfailurereason.md).
- [NSLocalizedRecoverySuggestionErrorKey](./user_info_dictionary_keys/api-1807767-nslocalizedrecoverysuggestionerr.md)
  The corresponding value is a string containing the localized recovery suggestion for the error. This string is suitable for displaying as the secondary message in an alert panel.
- [NSLocalizedRecoveryOptionsErrorKey](./user_info_dictionary_keys/api-1807774-nslocalizedrecoveryoptionserrork.md)
  The corresponding value is an array containing the localized titles of buttons appropriate for displaying in an alert panel. The first string is the title of the right-most and default button, the second the one to the left, and so on. The recovery options should be appropriate for the recovery suggestion returned by `localizedRecoverySuggestion`.
- [NSRecoveryAttempterErrorKey](./user_info_dictionary_keys/api-1807778-nsrecoveryattemptererrorkey.md)
  The corresponding value is an object that conforms to the NSErrorRecoveryAttempting informal protocol. The recovery attempter must be an object that can correctly interpret an index into the array returned by [`recoveryAttempter`](../../Foundation/nserror/recoveryattempter.md).
- [NSHelpAnchorErrorKey](./user_info_dictionary_keys/api-1807784-nshelpanchorerrorkey.md)
  The corresponding value is an [`NSString`](../../Foundation/nsstring.md) containing the localized help corresponding to the Help button. See [`helpAnchor`](../../Foundation/nserror/helpanchor.md) for more information.
- [NSURLErrorFailingURLErrorKey](./user_info_dictionary_keys/api-1807787-nsurlerrorfailingurlerrorkey.md)
  The corresponding value is an NSURL containing the URL which caused a load to fail. This key is only present in the [`NSURLErrorDomain`](../../Foundation/nsurlerrordomain.md).
- [NSURLErrorFailingURLStringErrorKey](./user_info_dictionary_keys/api-1807789-nsurlerrorfailingurlstringerrork.md)
  The corresponding value is an [`NSString`](../../Foundation/nsstring.md) object for the URL which caused a load to fail. This key is only present in the [`NSURLErrorDomain`](../../Foundation/nsurlerrordomain.md).
- [NSURLErrorFailingURLPeerTrustErrorKey](./user_info_dictionary_keys/api-1807791-nsurlerrorfailingurlpeertrusterr.md)
  The corresponding value is the [`SecTrust`](../../Security/sectrust.md) object representing the state of a failed SSL handshake. This key is only present in the [`NSURLErrorDomain`](../../Foundation/nsurlerrordomain.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmljs/tverror/user_info_dictionary_keys)*