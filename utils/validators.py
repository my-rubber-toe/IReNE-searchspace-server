"""
validators.py
=============
Handles the validations for the request using marshmallow.
"""
from marshmallow import validate, Schema, fields


class GetCollaboratorRequestValidator(Schema):
    """

    Request body schema for the endpoint /api/collabrequest/

    Parameters
    ----------
    Schema
        A JSON with the fields first_name, last_name and email and google token for validate the ISS

    Raises
    ------
    Validation Error
        If one of the fields is not valid
    """
    firstName = fields.String(required=True, validate=[
        validate.Length(min=1, max=30),
        validate.Regexp('^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- À-ÿ]*$')
        ])
    lastName = fields.String(required=True, validate=[
        validate.Length(min=1, max=30),
        validate.Regexp('^[A-ZÁÉÍÓÚÑÜ][a-z A-Z \- À-ÿ]*[a-záéíóúñü]$')])
    email = fields.Email(
        required=True,
        validate=[
            validate.Regexp('^[\.a-z0-9]*(@upr\.edu)$'),
            validate.Length(max=70)
        ]
    )
    idToken = fields.String(required=True)
