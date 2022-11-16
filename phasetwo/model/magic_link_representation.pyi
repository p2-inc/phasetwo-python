# coding: utf-8

"""
    Phase Two Admin REST API

    This is a REST API reference for the Phase Two Keycloak custom resources. These are extensions to the standard [Keycloak Admin REST API](https://www.keycloak.org/docs-api/17.0/rest-api/index.html).  ### Base URI format Paths specified in the documentation are relative to the the base URI. - Format: `https://<host>:<port>/auth/realms` - Example: `https://app.phasetwo.io/auth/realms`  ### Authentication Authentication is achieved by using the `Authentication: Bearer <token>` header in all requests. This is either the access token received from a normal authentication, or by a request directly to the OpenID Connect token endpoint.  It is recommended that you use a Keycloak Admin Client, such as [this one for Javascript](https://github.com/keycloak/keycloak-nodejs-admin-client), as they take care of authetication, getting an access token, and refreshing it when it expires.  #### Client credentials grant example ``` POST /auth/realms/test-realm/protocol/openid-connect/token Host: app.phasetwo.io Accept: application/json Content-type: application/x-www-form-urlencoded  grant_type=client_credentials&client_id=admin-cli&client_secret=fd649804-3a74-4d69-acaa-8f065c6b7da1 ```  #### Password grant example ``` POST /auth/realms/test-realm/protocol/openid-connect/token Host: app.phasetwo.io Accept: application/json Content-type: application/x-www-form-urlencoded  grant_type=password&username=uname@foo.com&password=pwd123AZY&client_id=admin-cli ```   # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from phasetwo import schemas  # noqa: F401


class MagicLinkRepresentation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "redirect_uri",
            "client_id",
            "email",
        }
        
        class properties:
            email = schemas.StrSchema
            client_id = schemas.StrSchema
            redirect_uri = schemas.StrSchema
            expiration_seconds = schemas.IntSchema
            force_create = schemas.BoolSchema
            send_email = schemas.BoolSchema
            __annotations__ = {
                "email": email,
                "client_id": client_id,
                "redirect_uri": redirect_uri,
                "expiration_seconds": expiration_seconds,
                "force_create": force_create,
                "send_email": send_email,
            }
    
    redirect_uri: MetaOapg.properties.redirect_uri
    client_id: MetaOapg.properties.client_id
    email: MetaOapg.properties.email
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["redirect_uri"]) -> MetaOapg.properties.redirect_uri: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiration_seconds"]) -> MetaOapg.properties.expiration_seconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["force_create"]) -> MetaOapg.properties.force_create: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["send_email"]) -> MetaOapg.properties.send_email: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["email", "client_id", "redirect_uri", "expiration_seconds", "force_create", "send_email", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client_id"]) -> MetaOapg.properties.client_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["redirect_uri"]) -> MetaOapg.properties.redirect_uri: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiration_seconds"]) -> typing.Union[MetaOapg.properties.expiration_seconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["force_create"]) -> typing.Union[MetaOapg.properties.force_create, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["send_email"]) -> typing.Union[MetaOapg.properties.send_email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["email", "client_id", "redirect_uri", "expiration_seconds", "force_create", "send_email", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        redirect_uri: typing.Union[MetaOapg.properties.redirect_uri, str, ],
        client_id: typing.Union[MetaOapg.properties.client_id, str, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        expiration_seconds: typing.Union[MetaOapg.properties.expiration_seconds, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        force_create: typing.Union[MetaOapg.properties.force_create, bool, schemas.Unset] = schemas.unset,
        send_email: typing.Union[MetaOapg.properties.send_email, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MagicLinkRepresentation':
        return super().__new__(
            cls,
            *_args,
            redirect_uri=redirect_uri,
            client_id=client_id,
            email=email,
            expiration_seconds=expiration_seconds,
            force_create=force_create,
            send_email=send_email,
            _configuration=_configuration,
            **kwargs,
        )