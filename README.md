# IyikaTrace
# 1. Summary
IyikaTrace is a digital platform built to track, trace, and verify the journey of agricultural products from the point of harvest to the end consumer — locally and internationally. Designed for transparency, compliance, and food safety, it will serve farmers, processors, exporters, and regulators.
By assigning unique trace IDs to produce batches and collecting data at each supply chain checkpoint, the platform empowers stakeholders with end-to-end visibility of product origin, handling, and compliance status.

# 2. Objectives
Digitally trace agricultural produce across all stages: production, aggregation, transportation, processing, warehousing, retail/export, and consumption
Ensure compliance with local and international standards, including EU, US, and Gulf markets
Create trust and transparency in agricultural value chains
Enable real-time verification by consumers, regulators, and off-takers
Offer custom traceability reports for exporters and agribusinesses

# 3. User Personas

| Persona             | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Smallholder Farmer  | Registers crops, harvest details, and generates QR code per batch          |
| Aggregator/Off-taker| Collects produce, logs handling details, transports to warehouse/processor |
| Warehouse Manager   | Logs receipt, checks conditions, updates chain of custody                   |
| Transporter         | Updates movement, logs transit data                                         |
| Processor           | Converts raw produce to value-added form, updates trace info               |
| Exporter            | Uploads compliance docs, links product to destination market requirements   |
| Inspector/Regulator | Reviews trace logs, approves or flags exports                              |
| Retailer            | Sells to final consumers, verifies product story                            |
| Consumer            | Scans QR code and verifies product origin, sustainability, and freshness   |

# 4. Functional Requirements

# 4.1 User Account Management
	•	Registration & login by user type
	•	Role-based dashboard access
	•	KYC verification for exporters/processors
 
# 4.2 Batch & Trace Code Management
	•	Batch creation with UUID (e.g., IT-BTCH-20250626-00001)
	•	QR code generation (printable/downloadable)
	•	NFC tag compatibility (future)
 
# 4.3 Trace Log System
Each touchpoint logs:
	•	Timestamp
	•	Actor ID
	•	Geo-location
	•	Photos (optional)
	•	Comments
	•	Environmental data (if available)
 
# 4.4 Chain of Custody Management
	•	Seamless transition from actor to actor
	•	Prevents backdating or overwriting of data
	•	Chain view accessible in timeline or tree format
 
# 4.5 Export Documentation Module
	•	Upload & link documents (PDF, image)
	•	Cert types: Phytosanitary, GAP, Organic, Country of Origin, Lab Test Reports
	•	Expiry management, alerts for near-expiry documents
 
# 4.6 QR Code Scanning System
	•	Instant display of trace history
	•	Language toggle (English, Hausa, French, Yoruba)
	•	Trust rating & verification status
 
# 4.7 Admin Dashboard
	•	User management
	•	Batch and trace audit trails
	•	Flagging or revoking non-compliant entries
	•	Analytics (location heatmaps, number of scans, top crops)

# 5. Non-Functional Requirements

| Requirement       | Description                                                                 |
|-------------------|-----------------------------------------------------------------------------|
| Performance       | System must support 10,000+ concurrent batch logs in MVP phase              |
| Scalability       | Modular microservice architecture for scale-up to other regions/countries   |
| Security          | End-to-end encryption, role-based access, audit logging                     |
| Offline Support   | Store-and-forward for mobile users in poor-connectivity zones               |
| Usability         | UX optimized for low-literacy users (icon-based UI, local language labels)  |
| Extensibility     | API-first design for partner integration (e.g., government, customs)        |

# 6. Compliance & Standards Support

| Regulation / Standard           | How IyikaTrace Complies                                           |
|----------------------------------|------------------------------------------------------------------|
| EU General Food Law              | Captures origin, traceability, hygiene data                      |
| US FDA FSMA (Produce Rule)       | Offers batch-level documentation, QR traceability                |
| GLOBALG.A.P.                     | Allows digital logging of GAP-relevant practices                 |
| Nigeria Quarantine Services      | Enables document uploads and certification tags                  |
| AFCTA Compliance                 | Includes traceability metadata for intra-Africa trade            |

# 7. System Architecture (MVP Phase)
Frontend:
	•	React Native App (Farmers, Aggregators, Transporters)
	•	React.js Web App (Admins, Exporters, Regulators)
Backend:
	•	Node.js with NestJS OR Django with FastAPI
	•	PostgreSQL + PostGIS (geolocation)
	•	Redis (caching, job queues)
	•	Firebase/Socket.io (for real-time logs)
Other Components:
	•	QR Generator Service (internal microservice)
	•	File Storage: AWS S3 or Cloudinary
	•	Push Notifications: Firebase Cloud Messaging

# 8. Entity Relationship Model (Summary)

| Entity            | Key Attributes                                                                 |
|-------------------|--------------------------------------------------------------------------------|
| User              | ID, Role, Name, Phone, Email, Profile, KYC Docs                                |
| Batch             | ID, Crop Type, Quantity, Date Harvested, Location, QR Code Link                |
| Trace Log         | ID, Timestamp, User ID, Batch ID, Event Type, Location, Notes                  |
| Document          | ID, Type, Linked Batch, Issuer, Expiry Date, File URL                          |
| Chain of Custody  | Origin, Destination, Timestamps, Handover Actor IDs                            |

# 9. Testing Plan

| Test Type          | Details                                                                      |
|--------------------|------------------------------------------------------------------------------|
| Unit Tests         | Core logic: batch creation, trace logs, QR generator                         |
| Integration Tests  | Actor-to-actor transitions, document uploads, location checks                |
| UX Testing         | Field-based with smallholder farmers                                         |
| API Testing        | REST endpoints + webhook integration                                         |
| Security Testing   | Role access simulation, injection prevention                                 |
| Performance Testing| Batch processing simulation under scale                                      |

# 10. Deployment Strategy

| Stage      | Platform                                                |
|------------|---------------------------------------------------------|
| Dev        | Local Docker + Railway                                  |
| Staging    | Vercel for frontend, Render/Fly.io for backend          |
| Production | AWS or GCP (with CI/CD)                                 |
| Monitoring | Sentry + Grafana + LogRocket                            |

# 11. MVP Timeline

| Phase               | Duration | Deliverables                                        |
|---------------------|----------|-----------------------------------------------------|
| Phase 1 – Design    | 2 weeks  | PRD, wireframes, UI/UX prototype                    |
| Phase 2 – Core Dev  | 6 weeks  | Batch engine, QR module, role dashboards            |
| Phase 3 – Pilot Launch | 2 weeks  | Farm-to-market trial with local farmers          |
| Phase 4 – Feedback  | 2 weeks  | Bug fixes, usability improvements                   |
| Phase 5 – Export Layer | 3 weeks  | Document module, country compliance tags         |

# 12. Future Phases

| Feature/Module           | Priority | Description                                           |
|--------------------------|----------|-------------------------------------------------------|
| Blockchain Integration   | High     | Immutable logging, verifiability                      |
| Cold Chain Monitoring    | Medium   | IoT sensor integration                                |
| Smart Contract Payments  | Medium   | B2B and producer-offtaker automation                  |
| Open API for Government  | High     | API integration with ministries/customs               |
| Traceability-as-a-Service| High     | Offer SaaS model to processors and exporters          |
| ML Anomaly Detection     | Low      | Identify suspicious activities in supply chain        |

# 13. Business Goals (12-Month Outlook)
	•	10,000 produce batches logged
	•	200 registered smallholder farmers
	•	50 registered exporters and aggregators
	•	25 local/foreign agribusiness clients
	•	Policy integration with 1 government agency
	•	First revenue milestone from SaaS/export clients

## License

This project is proprietary software developed by **CodeGreenAfrica**.  
All rights reserved. You may not use, copy, modify, or distribute this code  
without explicit permission.  
