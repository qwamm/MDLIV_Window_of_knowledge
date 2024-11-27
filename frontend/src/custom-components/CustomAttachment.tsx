import { useEffect } from "react";
import type { ChannelFilters, ChannelSort, StreamChat } from "stream-chat";

import { Attachment, type AttachmentProps } from "stream-chat-react";

export type CustomAttachmentType = {
    image: string;
    name: string;
    type: string;
    url: string;
};

export const attachments: CustomAttachmentType[] = [
    {
        image:
            "https://images-na.ssl-images-amazon.com/images/I/71k0cry-ceL._SL1500_.jpg",
        name: "iPhone",
        type: "product",
        url: "https://goo.gl/ppFmcR",
    },
];

export const CustomAttachment = (props: AttachmentProps) => {
    const { attachments } = props;
    const [attachment] = (attachments || []) as CustomAttachmentType[];
    if (attachment?.type === "product") {
        return (
            <div>
                Product:
                <a href={attachment.url} rel="noreferrer">
                    <img alt="custom-attachment" height="100px" src={attachment.image} />
                    <br />
                    {attachment.name}
                </a>
            </div>
        );
    }

    return <Attachment {...props} />;
};

export const useInitAttachmentMessage = ({
                                             filters,
                                             sort,
                                             client,
                                         }: {
    client: StreamChat;
    filters: ChannelFilters;
    sort: ChannelSort;
}) => {
    useEffect(() => {
        if (!client) return;

        const initAttachmentMessage = async () => {
            const [channel] = await client.queryChannels(filters, sort);

            await channel.sendMessage({
                text: "Your selected product is out of stock, would you like to select one of these alternatives?",
                attachments,
            });
        };

        initAttachmentMessage().catch((error) => {
            console.error(`Failed to initialize attachments`, error);
        });
    }, [client]);
};
