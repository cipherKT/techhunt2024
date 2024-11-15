'use client'
import Image from "next/image";
// import SuspeciousFlag from "../components/page";
import SuspeciousFlag from "../components/Landing";
import { Suspense } from 'react'


export default function Home() {
  return (
    <Suspense>
      <SuspeciousFlag />
    </Suspense>
  );
}
