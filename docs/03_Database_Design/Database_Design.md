# Database Design

## Database Tables

### Users

- id
- username
- email
- password_hash
- created_at

### Projects

- id
- title
- description
- image_url
- github_url
- live_demo_url
- technologies
- created_at

### Skills

- id
- skill_name
- proficiency

### Experiences

- id
- company
- position
- description
- start_date
- end_date

### Education

- id
- school
- degree
- start_year
- end_year

### Certificates

- id
- certificate_name
- issuing_organization
- issue_date
- credential_url

### Messages

- id
- name
- email
- subject
- message
- created_at

### Social Links

- id
- platform
- url
