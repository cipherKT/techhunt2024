"use client"

import {setToken} from "@/actions/setToken";
import {useEffect} from "react";
import Link from "next/link";
import {Button} from "@/components/ui/button";

export default async function Home() {
    useEffect(() => {
        const setTokenAsync = async () => {
            await setToken();
        };
        setTokenAsync();
    }, []);
    return (
        <>
            <Link href={"/flag"}>
                <Button>
                    🏳️Flag
                </Button>
            </Link>
        </>
    );
}
