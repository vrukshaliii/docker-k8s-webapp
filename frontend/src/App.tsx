// import { Button } from "./components/ui/button";
import { Menubar, MenubarMenu, MenubarTrigger } from "@/components/ui/menubar";
import { Separator } from "@/components/ui/separator";

export default function App() {
    return (
        <>
            <Menubar>
                <MenubarMenu>
                    <MenubarTrigger>Containers</MenubarTrigger>
                </MenubarMenu>
                <MenubarMenu>
                    <MenubarTrigger>Images</MenubarTrigger>
                </MenubarMenu>
                <MenubarMenu>
                    <MenubarTrigger>Volumes</MenubarTrigger>
                </MenubarMenu>
            </Menubar>
            <div className="container mt-10">
                <div className="space-y-2">
                    <h4 className="text-sm font-medium leading-none">
                        What are Containers?
                    </h4>
                    <p className="text-sm text-muted-foreground">
                        A Docker container image is a lightweight, standalone,
                        ...
                    </p>
                </div>
                <Separator className="my-2 max-w-sm" />
                <div className="flex h-5 items-center space-x-4 text-sm">
                    <div>Blog</div>
                    <Separator orientation="vertical" />
                    <div>Docs</div>
                    <Separator orientation="vertical" />
                    <div>Source</div>
                </div>
            </div>
        </>
    );
}
