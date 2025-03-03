// index.js - Home Page

import React from 'react';
import Head from 'next/head';

export default function Home() {
  return (
    <div className="container mx-auto p-4">
      <Head>
        <title>UCODTS - Unified Crew & Operations Digital Twin System</title>
        <meta name="description" content="Unified Crew & Operations Digital Twin System for enhanced airline operations." />
      </Head>
      <main>
        <h1 className="text-4xl font-bold text-center mb-8">Welcome to UCODTS</h1>
        <p className="text-center">Transforming airline operations with real-time insights and proactive management.</p>
        {/* Navigation links to other pages can be added here */}
      </main>
    </div>
  );
}
