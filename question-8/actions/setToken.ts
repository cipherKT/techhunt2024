"use server"

import {cookies} from "next/headers";
import {SignJWT} from "jose";

async function signJWT(payload: any) {
    const secret = new TextEncoder().encode(process.env.AUTH_SECRET);
    const alg = "HS256";

    return await new SignJWT(payload)
        .setProtectedHeader({alg})
        .setIssuedAt()
        .setExpirationTime("4w")
        .sign(secret);
}

export async function setToken() {
    const payload = {
        id: "00919531852385",
        role: "user"
    }

    const token = await signJWT(payload);

    cookies().set("token", token)
}