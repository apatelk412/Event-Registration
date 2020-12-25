ContactsList = [{'name': 'Alice Brown', 'email': '', 'phone': '1231112223'},
           {'name': 'Bob Crown', 'email': 'bob@crowns.com', 'phone': ''},
           {'name': 'Carlos Drew', 'email': 'carl@drewess.com', 'phone': '3453334445'},
           {'name': 'Doug Emerty', 'email': '', 'phone': '4564445556'},
           {'name': 'Egan Fair', 'email': 'eg@fairness.com', 'phone': '5675556667'}]

LeadsList = [{'name': '', 'email': 'kevin@keith.com', 'phone': ''},
         {'name': 'Lucy', 'email': 'lucy@liu.com', 'phone': '3210001112'},
         {'name': 'Mary Middle', 'email': 'mary@middle.com', 'phone': '3331112223'},
         {'name': '', 'email': '', 'phone': '4442223334'},
         {'name': '', 'email': 'ole@olson.com', 'phone': ''}]


import json


class CreateRegistration():
    def create_contact(self, event_details):
        name = event_details['registrant'].get('name')
        email = event_details['registrant'].get('email')
        phone = event_details['registrant'].get('phone')
        for contact in ContactsList:
            if email in contact.get('email') or phone in contact.get('phone'):
                if not contact.get('name'):
                    contact['name'] = name
                if not contact.get('email'):
                    contact['email'] = email
                if not contact.get('phone'):
                    contact['phone'] = phone
        for lead in LeadsList:
            if email in lead.get('email') or phone in lead.get('phone'):
                if not lead.get('name'):
                    lead['name'] = name
                if not lead.get('email'):
                    lead['email'] = email
                if not lead.get('phone'):
                    lead['phone'] = phone
                ContactsList.append(lead)
                LeadsList.remove(lead)
        if not any(contact['email'] == email for contact in ContactsList) and \
                not any(contact['phone'] == phone for contact in ContactsList) and \
                not any(lead['email'] == email for lead in LeadsList) and \
                not any(lead['phone'] == phone for lead in LeadsList):
            ContactsList.append({'name':name, 'email':email, 'phone':phone})
        print("\nContactsList------>", ContactsList)
        print("\nLeadsList------>", LeadsList)



s = CreateRegistration()
new_event_registartion = [
{
    "registrant":
        {
            "name": "Lucy Liu",
            "email": "lucy@liu.com",
            "phone": "None",
        }
},
{
    "registrant":
        {
            "name": "Doug",
            "email": "doug@emmy.com",
            "phone": "4564445556",
        }
},
{
    "registrant":
        {
            "name": "Uma Thurman",
            "email": "uma@thurs.com",
            "phone": "None",
        }
}]

for rec in new_event_registartion:
    s.create_contact(rec)

