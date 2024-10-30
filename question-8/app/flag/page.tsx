import {cookies} from "next/headers";

function decodeBase64JWT(token: string) {
    const parts = token.split(".");
    return JSON.parse(Buffer.from(parts[1], "base64").toString());
}

export default async function Flag() {
    const token = cookies().get("token")?.value;

    if (!token) {
        return <div>You must be a power user to access this page!</div>
    } else if (decodeBase64JWT(token).role !== "power") {
        return <div>You must be a power user to access this page!</div>
    } else {
        return <div>Flag: {process.env.FLAG}</div>
    }
}