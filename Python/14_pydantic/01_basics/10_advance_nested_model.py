"""_performance_consideration_
    1. Deep nesting impacts performance - Keep reasonable depth
    2. Large lists of nested models - Consider pagination
    3. Circular references - Use carefully, can cause memory issues
    4. Lazy loading - Consider for expensive nested computations
"""
"""_data_modeling_tips_
    1. Model real-world relationships - Mirror your domain structure
    2. Use Optional appropriately - Not all relationships are required
    3. Consider Union types - For polymorphic relationships
    4. Validate business rules - Use model validators for cross-model logic
"""

from pydantic import BaseModel
from typing import Optional, List, Union

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None


class TextConent(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    sections: List[Union[TextConent, ImageContent]]


class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    postal_code: str

class Organization(BaseModel):
    name: str
    head_quarter: Address
    branches: List[Address]=[]