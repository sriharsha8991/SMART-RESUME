An intial API setup the Mongo DB where user Creates profile 

Sample Payload look like something as follows :

``` json
{
  "_id": "ObjectId",
  "full_name": "Sriharsha Velicheti",
  "email": "sriharsha@email.com",
  "phone": "+91-8309012139",
  "dob": "2000-01-01",
  "location": "Bangalore, India",
  "career_objective": "To become a skilled AI Engineer with expertise in multimodal systems.",
  "education": [
    {
      "degree": "B.Tech in CSE (Data Science)",
      "institution": "Jain University",
      "start_year": 2019,
      "end_year": 2023,
      "cgpa": 8.75
    }
  ],
  "skills": ["Python", "FastAPI", "MongoDB", "LangChain", "OpenAI", "Git"],
  "projects": [
    {
      "title": "AI Resume Builder",
      "description": "Built an AI-powered resume builder using GPT and MongoDB.",
      "tech_stack": ["FastAPI", "OpenAI", "MongoDB"],
      "github_url": "https://github.com/username/project"
    }
  ],
  "certifications": [
    {
      "title": "NPTEL Python for Data Science",
      "issuer": "IIT Madras",
      "year": 2022
    }
  ],
  "experience": [
    {
      "role": "Generative AI Intern",
      "company": "Siemens",
      "duration": "3 months",
      "description": "Built a healthcare assistant using Gemini and RAG pipelines."
    }
  ],
  "contributions": [
    {
      "type": "Open Source",
      "title": "LangChain Plugin PR",
      "description": "Contributed to LangChain plugin support",
      "link": "https://github.com/langchain-ai/langchain/pull/xyz"
    }
  ],
  "github_url": "https://github.com/sriharsha",
  "linkedin_url": "https://linkedin.com/in/sriharsha",
  "resume_link": "https://resume-bucket.s3.amazonaws.com/sriharsha-resume.pdf",
  "interests": ["AI Research", "Public Speaking", "System Design"],
  "languages": ["English", "Hindi", "Telugu"],
  "created_at": "ISODate",
  "updated_at": "ISODate"
}

```