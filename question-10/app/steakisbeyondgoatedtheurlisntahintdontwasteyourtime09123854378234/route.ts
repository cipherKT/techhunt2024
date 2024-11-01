import {NextResponse} from "next/server";

export async function GET() {
    try {
        const smth = await fetch('https://api.uploadthing.com/v6/listFiles', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Uploadthing-Api-Key': process.env.UPLOADTHING_API_KEY!
            },
            body: JSON.stringify({})
        })

        const resp = await smth.json()
        console.log(resp.files[0].key)
        const smth1 = await fetch('https://api.uploadthing.com/v6/requestFileAccess', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-Uploadthing-Api-Key': process.env.UPLOADTHING_API_KEY!
            },
            body: JSON.stringify({
                fileKey: resp.files[0].key
            })
        })

        const resp1 = await smth1.json()
        return NextResponse.redirect(resp1.url)
    } catch (e) {
        return NextResponse.json({error: "Contact Event Organizers"}, {status: 500})
    }
}