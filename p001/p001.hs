import System.Environment

p001 :: (Integral a) => a -> a
p001 n = (sum . Prelude.filter (\m -> mod m 3 == 0 || mod m 5 == 0)) [3..n-1]

main :: IO ()
main = do
    args <- getArgs
    putStrLn (show (p001 (read (head args) :: Int)))
