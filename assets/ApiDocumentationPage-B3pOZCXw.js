import{l as e}from"./utils-BdatOYwG.js";import{E as t,d as n}from"./vendor-react-Xxqe9L4J.js";import{t as r}from"./Icon-CsG5o18c.js";import{n as i,t as a}from"./FAQAccordion-DhEV1rRz.js";import{t as o}from"./SectionCard-DsHcWrcO.js";import{t as s}from"./CalloutBox-CDy9ktib.js";var c=e(t(),1),l=n(),u=()=>{let[e,t]=(0,c.useState)(!1),[n,u]=(0,c.useState)(`curl`),d=[{label:`Developer Hub`,href:`/docs/api`},{label:`REST & Vector API Specification`}],f=[{id:`auth`,title:`Authentication & API Keys`},{id:`search-endpoint`,title:`POST /v1/search/vector`},{id:`code-examples`,title:`Code Examples & SDK`},{id:`rate-limits`,title:`Rate Limits & Pagination`},{id:`errors`,title:`Error Response Format`},{id:`faq`,title:`Developer FAQ`}],p=[{title:`System Status Dashboard`,description:`Check real-time API endpoint uptime and latency metrics.`,href:`/system-status`,iconName:`grid`},{title:`Location Security`,description:`Review API telemetry encryption and token hashing.`,href:`/location-security`,iconName:`shield`}],m=[{question:`Where do I generate my Enterprise API key?`,answer:`API keys are provisioned inside the Nearby Developer Dashboard under Organization Settings > API Tokens.`},{question:`What is the default rate limit for REST API endpoints?`,answer:`Standard Developer tier allows 600 requests/minute. Enterprise SLA tiers support up to 50,000 requests/minute with custom dedicated clusters.`}],h={curl:`curl -X POST "https://api.nearby.ai/v1/search/vector" \\
  -H "Authorization: Bearer nb_live_9f8a3b2c1d0e" \\
  -H "Content-Type: application/json" \\
  -d '{
    "query": "quiet sunset beach spots near Panaji",
    "latitude": 15.498,
    "longitude": 73.834,
    "radius_km": 15,
    "max_results": 5
  }'`,ts:`import { NearbyClient } from '@nearby/sdk';

const client = new NearbyClient({
  apiKey: process.env.NEARBY_API_KEY,
});

const response = await client.search.vector({
  query: "quiet sunset beach spots near Panaji",
  latitude: 15.498,
  longitude: 73.834,
  radiusKm: 15,
  maxResults: 5,
});

console.log(response.places);`,python:`from nearby import NearbyClient
import os

client = NearbyClient(api_key=os.environ.get("NEARBY_API_KEY"))

response = client.search.vector(
    query="quiet sunset beach spots near Panaji",
    latitude=15.498,
    longitude=73.834,
    radius_km=15,
    max_results=5
)

for place in response.places:
    print(place.name, place.rating)`};return(0,l.jsxs)(i,{hero:{title:`Developer REST & Vector API Specs`,description:`Integrate Nearby's semantic travel search, real-time GIS radar, and itinerary planning APIs directly into your software applications.`,category:`Developer Platform`,iconName:`settings`,lastUpdatedDate:`July 26, 2026`,version:`v1.0.0 Enterprise API`},breadcrumbs:d,tocItems:f,relatedLinks:p,children:[(0,l.jsxs)(o,{id:`auth`,title:`Authentication & API Keys`,iconName:`shield`,badgeText:`Bearer Token`,children:[(0,l.jsxs)(`p`,{className:`text-xs text-muted-foreground leading-relaxed`,children:[`All API requests to Nearby endpoints must include an `,(0,l.jsx)(`code`,{className:`font-mono text-primary bg-muted px-1.5 py-0.5 rounded-sm`,children:`Authorization: Bearer YOUR_API_KEY`}),` header. Requests without valid bearer credentials return a `,(0,l.jsx)(`code`,{className:`font-mono text-rose-400`,children:`401 Unauthorized`}),` response.`]}),(0,l.jsxs)(s,{type:`security`,title:`API Key Security`,children:[`Never expose secret live keys (`,(0,l.jsx)(`code`,{className:`font-mono`,children:`nb_live_...`}),`) in client-side frontend code or public GitHub repositories. Use server-side proxy routes or restricted publishable keys.`]})]}),(0,l.jsxs)(o,{id:`search-endpoint`,title:`POST /v1/search/vector`,iconName:`sparkles`,badgeText:`Vector Search`,children:[(0,l.jsx)(`p`,{className:`text-xs text-muted-foreground leading-relaxed`,children:`Executes a high-dimensional vector search combining natural language query semantics with spatial coordinates.`}),(0,l.jsx)(`div`,{className:`space-y-2 my-2 font-mono text-xs`,children:(0,l.jsx)(`div`,{className:`p-3 rounded-sm border border-border/60 bg-zinc-950 text-zinc-200 space-y-1`,children:(0,l.jsxs)(`div`,{className:`flex items-center gap-2`,children:[(0,l.jsx)(`span`,{className:`font-bold text-emerald-400`,children:`POST`}),(0,l.jsx)(`span`,{className:`text-zinc-400`,children:`https://api.nearby.ai/v1/search/vector`})]})})})]}),(0,l.jsx)(o,{id:`code-examples`,title:`Code Examples & SDK Snippets`,iconName:`settings`,badgeText:`Multi-Language`,children:(0,l.jsxs)(`div`,{className:`rounded-sm border border-border/80 bg-zinc-950 overflow-hidden`,children:[(0,l.jsxs)(`div`,{className:`flex items-center justify-between border-b border-zinc-800 bg-zinc-900/90 px-4 py-2`,children:[(0,l.jsx)(`div`,{className:`flex items-center gap-2`,children:[`curl`,`ts`,`python`].map(e=>(0,l.jsx)(`button`,{type:`button`,onClick:()=>u(e),className:`rounded-sm px-3 py-1 font-mono text-xs font-bold uppercase transition-all ${n===e?`bg-emerald-500/20 text-emerald-400 border border-emerald-500/40`:`text-zinc-400 hover:text-white`}`,children:e===`ts`?`TypeScript`:e},e))}),(0,l.jsxs)(`button`,{type:`button`,onClick:()=>{navigator.clipboard.writeText(h[n]),t(!0),setTimeout(()=>t(!1),2e3)},className:`flex items-center gap-1 text-xs text-zinc-400 hover:text-white transition-colors`,children:[(0,l.jsx)(r,{name:e?`check`:`bookmark`,size:`xs`}),(0,l.jsx)(`span`,{children:e?`Copied!`:`Copy Code`})]})]}),(0,l.jsx)(`pre`,{className:`p-4 font-mono text-xs text-zinc-200 overflow-x-auto leading-relaxed`,children:(0,l.jsx)(`code`,{children:h[n]})})]})}),(0,l.jsxs)(o,{id:`rate-limits`,title:`Rate Limits & Pagination`,iconName:`clock`,badgeText:`HTTP Headers`,children:[(0,l.jsx)(`p`,{className:`text-xs text-muted-foreground leading-relaxed`,children:`Rate limits are enforced per API key. Every HTTP response contains standard rate-limiting headers:`}),(0,l.jsx)(`div`,{className:`space-y-2 my-2 font-mono text-xs`,children:(0,l.jsxs)(`div`,{className:`p-3 rounded-sm border border-border/60 bg-card/60 space-y-1`,children:[(0,l.jsxs)(`p`,{children:[(0,l.jsx)(`span`,{className:`text-primary font-bold`,children:`X-RateLimit-Limit:`}),` 600`]}),(0,l.jsxs)(`p`,{children:[(0,l.jsx)(`span`,{className:`text-amber-400 font-bold`,children:`X-RateLimit-Remaining:`}),` 598`]}),(0,l.jsxs)(`p`,{children:[(0,l.jsx)(`span`,{className:`text-emerald-400 font-bold`,children:`X-RateLimit-Reset:`}),` 1722000000`]})]})})]}),(0,l.jsxs)(o,{id:`errors`,title:`Error Response Format`,iconName:`error`,badgeText:`JSON Schema`,children:[(0,l.jsx)(`p`,{className:`text-xs text-muted-foreground leading-relaxed`,children:`Errors return standard RFC 7807 Problem Details envelopes:`}),(0,l.jsx)(`pre`,{className:`p-4 rounded-sm border border-border/80 bg-zinc-950 font-mono text-xs text-rose-300 overflow-x-auto`,children:`{
  "type": "https://api.nearby.ai/errors/rate-limit-exceeded",
  "title": "Rate Limit Exceeded",
  "status": 429,
  "detail": "Quota of 600 requests per minute exceeded. Retry after 14 seconds.",
  "instance": "/v1/search/vector"
}`})]}),(0,l.jsx)(o,{id:`faq`,title:`Developer FAQ`,iconName:`info`,badgeText:`Help`,children:(0,l.jsx)(a,{items:m})})]})};export{u as ApiDocumentationPage,u as default};