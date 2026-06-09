# Apple School Manager and Apple Business APIs changelog

**Framework**: Apple School Manager and Apple Business APIs

Learn about new features and updates in the Apple School Manager and Apple Business APIs.

##### Overview

Use this changelog to learn about feature updates, deprecations, and removals for the Apple School Manager and Apple Business APIs.

##### 21 202663

New features for the Apple Business APIs

Added support for managing device management services using the following endpoints:

- [`Get Device Management Service Information.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-mdmserver-information)
- [`Create a Device Management Service.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/create-an-mdmserver)
- [`Update a Device Management Service.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/update-an-mdmserver)
- [`Delete a Device Management Service.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/delete-an-mdmserver)

##### 20 2026414

New features for the Apple Business APIs

Added the following endpoints:

- Audit events (to query organization audit events with filtering support) - [`Retrieve a list of audit events for an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-audit-events)
- User and user group management services - [`Get a list of users in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-users)
- [`Get information about a specific user in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-user-information)
- [`Get a list of user groups in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-user-groups)
- [`Get information about a specific user group in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-usergroup-information)
- [`Get a list of users assigned to a user group in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-all-user-ids-for-a-user-group)
- Apps and packages - [`Get the licensed apps in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-apps)
- [`Get information about a specific app in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-app-information)
- [`Get packages in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-packages)
- [`Get information about a specific package in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-package-information)

Added full Configuration management: create, read, update, delete, and support for custom Configurations

- [`Get the list of Configurations in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-configurations)
- [`Get the details of a Configuration in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-configuration-information)
- [`Create a Configuration in an organization (of type CUSTOM_SETTING).`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/create-a-configuration)
- [`Update a Configuration in an organization (of type CUSTOM_SETTING).`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/update-a-configuration)
- [`Delete a Configuration in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/delete-a-configuration)

Added full Blueprint management: create, read, update, delete, and endpoints to manage Blueprint relationships with apps, packages, configurations, devices, users, and user groups

- [`Get a list of Blueprints in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-blueprints)
- [`Create a Blueprint in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/create-a-blueprint)
- [`Get information about a Blueprint in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-blueprint-information)
- [`Update a Blueprint in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/update-a-blueprint)
- [`Delete a Blueprint in an organization.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/delete-a-blueprint)
- [`Get a list of app IDs associated with a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-all-app-ids-for-a-blueprint)
- [`Add apps to a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/add-apps-to-a-blueprint)
- [`Remove apps from a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/remove-apps-from-a-blueprint)
- [`Get a list of Configuration IDs associated with a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-all-configuration-ids-for-a-blueprint)
- [`Add Configurations to a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/add-configurations-to-a-blueprint)
- [`Remove Configurations from a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/remove-configurations-from-a-blueprint)
- [`Get a list of package IDs associated with a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-all-package-ids-for-a-blueprint)
- [`Add packages to a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/add-packages-to-a-blueprint)
- [`Remove packages from a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/remove-packages-from-a-blueprint)
- [`Get a list of device IDs associated with a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-all-orgdevice-ids-for-a-blueprint)
- [`Add devices to a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/add-org-devices-to-a-blueprint)
- [`Remove devices from a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/remove-org-devices-from-a-blueprint)
- [`Get a list of user IDs associated with a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-all-user-ids-for-a-blueprint)
- [`Add users to a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/add-users-to-a-blueprint)
- [`Remove users from a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/remove-users-from-a-blueprint)
- [`Get a list of user group IDs associated with a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-all-user-group-ids-for-a-blueprint)
- [`Add user groups to a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/add-user-groups-to-a-blueprint)
- [`Remove user groups from a Blueprint.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/remove-user-groups-from-a-blueprint)

Added support for retrieving devices enrolled in the built-in device management service

- [`Get Devices Enrolled in the Apple Device Management Service.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-apple-mdm-enrolled-devices)

Added detailed device information for devices enrolled in the built-in device management service

- [`Get Details for a Device Enrolled in the Apple Device Management Service.`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessapi/get-the-details-for-apple-mdm-enrolled-device)

##### 15 2026120

Changes

- Updated Python script example to use PwJWT in the article [`Implementing OAuth for the Apple School and Business Manager API`](https://developer.apple.comhttps://developer.apple.com/documentation/apple-school-and-business-manager-api/implementing-oauth-for-the-apple-school-and-business-manager-api)
- Updated MAC address types in Apple School Manager [`OrgDevice.Attributes`](https://developer.apple.comhttps://developer.apple.com/documentation/appleschoolmanagerapi/orgdevice/attributes-data.dictionary).
- Updated MAC address types in Apple Business [`OrgDevice.Attributes`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessmanagerapi/orgdevice/attributes-data.dictionary).

##### 14 20251217

New features

- Added Wi-Fi, Bluetooth, and built-in Ethernet MAC address attributes for macOS to the [`OrgDevice.Attributes`](https://developer.apple.comhttps://developer.apple.com/documentation/appleschoolmanagerapi/orgdevice/attributes-data.dictionary)
- Added Wi-Fi, Bluetooth, and built-in Ethernet MAC address attributes for macOS to the [`OrgDevice.Attributes`](https://developer.apple.comhttps://developer.apple.com/documentation/appleschoolmanagerapi/orgdevice/attributes-data.dictionary)

##### 13 2025115

New features

- Added AppleCare content to the [`Apple School Manager API`](https://developer.apple.comhttps://developer.apple.com/documentation/appleschoolmanagerapi/get-all-apple-care-coverage-for-an-orgdevice)
- Added AppleCare content to the [`Apple Business API`](https://developer.apple.comhttps://developer.apple.com/documentation/applebusinessmanagerapi/get-all-apple-care-coverage-for-an-orgdevice)

##### 12 20250716

New features

- Added Wi-Fi and Bluetooth MAC address attributes for iOS, iPadOS, tvOS, and visionOS to the [`OrgDevice.Attributes`](https://developer.apple.comhttps://developer.apple.com/documentation/appleschoolmanagerapi/orgdevice/attributes-data.dictionary)
- Added Wi-Fi and Bluetooth MAC address attributes for iOS, iPadOS, tvOS, and visionOS to the [`OrgDevice.Attributes`](https://developer.apple.comhttps://developer.apple.com/documentation/appleschoolmanagerapi/orgdevice/attributes-data.dictionary)

##### 11 20250710

Changes

- Updated content in the article [`Implementing OAuth for the Apple School and Business Manager API`](https://developer.apple.comhttps://developer.apple.com/documentation/apple-school-and-business-manager-api/implementing-oauth-for-the-apple-school-and-business-manager-api)


---

*[View on Apple Developer](https://developer.apple.com/documentation/apple-school-and-business-manager-api/apple-school-manager-and-apple-business-api-changelog)*