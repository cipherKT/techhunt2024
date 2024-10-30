'use client'
import Image from "next/image";
import Landing from "../components/Landing";
import { Suspense } from 'react'


export default function Home() {
  return (
    <Suspense>
      <Landing />
    </Suspense>
  );
}
